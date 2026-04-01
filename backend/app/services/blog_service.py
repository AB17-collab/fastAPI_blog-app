from sqlalchemy.orm import Session
from app.repositories import blog_repo

def create_blog(db: Session, user_id: int, request):
    return blog_repo.create_blog(db, user_id, request)

def get_all(db: Session):
    return blog_repo.get_all_blogs(db)