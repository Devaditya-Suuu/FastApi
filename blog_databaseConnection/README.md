# blog_databaseConnection

A simple **FastAPI** CRUD application that demonstrates how to connect a REST API to a **SQLite** database using **SQLAlchemy ORM** and **Pydantic** for data validation.

---

## Concepts Covered

| Concept | Description |
|---|---|
| **FastAPI** | Web framework for building REST APIs in Python |
| **SQLAlchemy ORM** | Maps Python classes to database tables |
| **SQLite** | Lightweight file-based SQL database |
| **Pydantic** | Validates incoming request data using Python type hints |
| **Dependency Injection** | `Depends(get_db)` provides a DB session per request |
| **HTTPException** | Returns proper HTTP error responses (e.g., 404) |

---

## Project Structure

```
blog_databaseConnection/
├── __init__.py       # Marks directory as a Python package (enables relative imports)
├── main.py           # FastAPI app — defines all API routes/endpoints
├── database.py       # SQLAlchemy setup — DB engine, session factory, and Base
├── model.py          # ORM model — defines the 'blogs' database table
├── schemas.py        # Pydantic schema — validates incoming request body
└── README.md         # This file
```

---

## How It Works

### 1. `database.py` — Database Connection
- Creates a SQLite database file (`blog.db`) in the project root.
- Sets up an **engine** (the DB connection) and **SessionLocal** (session factory).
- `Base` is the parent class for all ORM models.

### 2. `model.py` — Database Table
- Defines the `Blog` ORM model which maps to the `blogs` table.
- Columns: `id` (auto-increment primary key), `title` (string), `body` (string).
- SQLAlchemy auto-creates this table on startup via `Base.metadata.create_all(engine)`.

### 3. `schemas.py` — Request Validation
- Defines a Pydantic `blog` schema that validates POST request bodies.
- Ensures `title` and `body` are present and are strings before touching the DB.

### 4. `main.py` — API Routes
- Wires everything together and exposes 4 endpoints.

---

## API Endpoints

| Method | Route | Description | Status Code |
|---|---|---|---|
| `POST` | `/blog` | Create a new blog post | `201 Created` |
| `GET` | `/blog` | Retrieve all blog posts | `200 OK` |
| `GET` | `/blog/{id}` | Retrieve a single blog post by ID | `200 OK` / `404 Not Found` |
| `DELETE` | `/blog/{id}` | Delete a blog post by ID | `204 No Content` |

---

## Running the App

Make sure you are in the **project root** (`fastapi-env/`), not inside this folder:

```bash
cd /path/to/fastapi-env
uvicorn blog_databaseConnection.main:app --reload
```

> Running from inside the `blog_databaseConnection/` folder will cause a `ModuleNotFoundError` because relative imports (`from . import model`) require the directory to be treated as a package from the parent.

---

## Interactive API Docs

Once running, visit:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Dependencies

- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `pydantic`
