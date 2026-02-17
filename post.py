from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    """Home route."""
    return {'data': 'blog list'}


class Blog(BaseModel):
    """Blog request model using Pydantic for validation."""
    title: str
    description: Optional[str] = None
    body: str
    published_at: Optional[str] = None


@app.post('/blog')
async def create_blog(blog: Blog):
    """
    Create a new blog post.
    
    Request body is automatically validated against the Blog model.
    """
    return {'data': f'Blog created with title: {blog.title}'}