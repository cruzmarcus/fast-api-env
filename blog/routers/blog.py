from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models, oauth2
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy_blog(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(id, request, db)


@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.get_an_blog_by_id(id, db)
