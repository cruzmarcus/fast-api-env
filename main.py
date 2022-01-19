from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} blog list from the database'}
    else:
        return {'data': f'{limit} blog list from the database'}


@app.get("/blog/unpublished")
def unpubliched():
    return {'data': 'all unpubliched blogs'}


@app.get("/blog/{id}")
def about(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    # fetch comments of blog with id = id
    return limit
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", host="localhost", port=9000
    )
