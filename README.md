# FastAPI Blog API

A simple REST API built with FastAPI to demonstrate basic routing concepts including path parameters, query parameters, and optional parameters.

## Features

- Fast and modern Python web framework
- Automatic API documentation (Swagger UI)
- Type hints and validation
- Query parameters with default values
- Path parameters with type validation
- Optional parameters

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Devaditya-Suuu/fastapi-env.git
   cd fastapi-env
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .
   source bin/activate  # On macOS/Linux
   # or
   .\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Server

Start the development server with auto-reload:

```bash
python -m uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## API Endpoints

### Home
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns blog list message |

### Blogs
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/blog` | Get blogs with optional filters |
| GET | `/blog/something` | Static route example |
| GET | `/blog/{id}` | Get a specific blog by ID |
| GET | `/blog/{id}/comments` | Get comments for a blog |

### Query Parameters for `/blog`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | int | 10 | Number of blogs to return |
| `published` | bool | true | Filter by published status |
| `sort` | str | None | Optional sorting parameter |

**Examples:**
```bash
# Get 10 published blogs (default)
curl http://127.0.0.1:8000/blog

# Get 50 blogs
curl "http://127.0.0.1:8000/blog?limit=50"

# Get 20 unpublished blogs
curl "http://127.0.0.1:8000/blog?limit=20&published=false"

# Get blog with ID 5
curl http://127.0.0.1:8000/blog/5

# Get comments for blog ID 3
curl http://127.0.0.1:8000/blog/3/comments
```

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Project Structure

```
fastapi-env/
├── main.py          # Main application file with all routes
├── README.md        # This file
├── .gitignore       # Git ignore file
├── bin/             # Virtual environment binaries
├── lib/             # Virtual environment libraries
└── include/         # Virtual environment includes
```

## Key Concepts Demonstrated

### 1. Path Parameters
```python
@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}
```

### 2. Query Parameters with Defaults
```python
@app.get('/blog')
def get_blogs(limit: int = 10, published: bool = True):
    return {'data': f'{limit} blogs'}
```

### 3. Optional Parameters
```python
from typing import Optional

@app.get('/blog')
def get_blogs(sort: Optional[str] = None):
    # sort is optional and defaults to None
    pass
```

### 4. Route Order Matters
Static routes (like `/blog/something`) should be defined **before** dynamic routes (like `/blog/{id}`) to avoid conflicts.

## License

MIT

## Author

Devaditya
