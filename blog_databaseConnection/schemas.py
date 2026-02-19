# schemas.py
# This file defines Pydantic schemas (data validation models).
# Schemas are used to validate incoming request data before it touches the database.
# They are separate from SQLAlchemy models — schemas handle the shape of data
# coming IN (requests) and going OUT (responses), while models handle the DB structure.

from pydantic import BaseModel

# The 'blog' schema defines what the request body must look like
# when a client sends data to create or interact with a blog post.
# Pydantic will automatically validate types and raise errors if the data is wrong.
class blog(BaseModel):
    title: str  # The blog title — must be a string
    body: str   # The blog body/content — must be a string