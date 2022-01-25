from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


def get_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_an_blog_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the {id} is not available"
        )

    return blog


def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} not found"
        )

    blog.delete(synchronize_session=False)
    db.commit()

    return {"data": f"Delete blog with the id {id} was done"}


def update_blog(id: int, request: schemas.Blog, db: Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} not found"
        )

    blog.update(request.dict())
    db.commit()

    return request.dict()
