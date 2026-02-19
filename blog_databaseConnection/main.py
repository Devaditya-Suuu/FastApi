# main.py
# This is the entry point of the FastAPI application.
# It defines all the API routes (endpoints) and connects them to the database.
# FastAPI uses these route definitions to automatically generate interactive
# API documentation at /docs (Swagger UI) and /redoc.

from fastapi import FastAPI, Depends, Response, status, HTTPException
from . import schemas       # Pydantic schemas for request body validation
from . import model         # SQLAlchemy ORM models (database table definitions)
from .database import engine, SessionLocal  # DB engine and session factory

from sqlalchemy.orm import Session

# Create the FastAPI application instance.
# All routes are registered on this 'app' object.
app = FastAPI()

# This line creates all the tables defined in our models (if they don't already exist).
# SQLAlchemy reads the Base metadata and issues CREATE TABLE SQL statements.
model.Base.metadata.create_all(engine)


# --- Dependency: get_db ---
# This is a FastAPI dependency that provides a database session to each request.
# 'yield' makes it a generator — FastAPI will:
#   1. Create a new DB session before the request
#   2. Inject it into the route function via Depends(get_db)
#   3. Close the session after the request finishes (in the 'finally' block)
# This ensures no DB connections are leaked.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- POST /blog ---
# Creates a new blog post in the database.
# 'request' is validated against the schemas.blog Pydantic model.
# Steps: create a model instance → add to session → commit → refresh to get DB-generated fields.
# Returns HTTP 201 Created on success.
@app.post('/blog', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.blog, db: Session = Depends(get_db)):
    new_blog = model.Blog(title=request.title, body=request.body)
    db.add(new_blog)        # Stage the new record
    db.commit()             # Save it to the database
    db.refresh(new_blog)    # Reload from DB to get the auto-generated 'id'
    return new_blog


# --- GET /blog ---
# Retrieves all blog posts from the database.
# db.query(model.Blog).all() translates to: SELECT * FROM blogs
@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs


# --- GET /blog/{id} ---
# Retrieves a single blog post by its ID.
# {id} is a path parameter — FastAPI extracts it from the URL and passes it as 'id'.
# If no blog is found with that ID, we raise an HTTPException with 404 status.
# This is the correct FastAPI pattern — raising HTTPException immediately stops
# the request and returns a proper error response to the client.
@app.get('/blog/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} not found'
        )
    return blog


# --- DELETE /blog/{id} ---
# Deletes a blog post from the database by its ID.
# synchronize_session=False tells SQLAlchemy not to update the in-memory session
# objects after deletion — this is fine here since we don't use the session after.
# Returns HTTP 204 No Content on success (standard for DELETE operations).
@app.delete('/blog/{id}', status_code=204)
def destroy(id: int, db: Session = Depends(get_db)):
    db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

