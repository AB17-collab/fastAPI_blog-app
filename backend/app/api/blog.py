from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import blog_service

router = APIRouter(prefix="/blogs")

@router.post("/")
def create_blog(request, db: Session = Depends(get_db)):
    return blog_service.create_blog(db, user_id=1, request=request)

@router.get("/")
def get_blogs(db: Session = Depends(get_db)):
    return blog_service.get_all(db)