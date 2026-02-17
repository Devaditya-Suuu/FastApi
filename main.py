from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    """Home route - returns blog list."""
    return {'data': 'blog list'}

@app.get('/blog')
def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    """
    Get blogs with optional filtering.
    
    Query Parameters:
        - limit: Number of blogs to return (default: 10)
        - published: Filter by published status (default: True)
        - sort: Optional sorting field (use Optional[T] for non-required params)
    """
    if published:
        return {'data': f'{limit} published blogs from the list'}
    else:
        return {'data': f'{limit} blogs from the list'}

# Note: Static routes must be defined BEFORE dynamic routes.
# If this route were placed after /blog/{id}, FastAPI would try to parse "something" as an int.
@app.get('/blog/something')
def something():
    """Static route example."""
    return {'data': 'something'}

@app.get('/blog/{id}')
def show(id: int):
    """Get a single blog by ID (path parameter)."""
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    """
    Get comments for a blog.
    
    FastAPI distinguishes path vs query parameters automatically:
    - 'id' is in the path -> path parameter
    - 'limit' is not in the path -> query parameter
    """
    return {'data': ['comment 1', 'comment 2'], 'limit': limit}


