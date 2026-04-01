from sqlalchemy.orm import Session
from app.models.models import Blog

def create_blog(db: Session, user_id: int, data):
    blog = Blog(**data.dict(), user_id=user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_all_blogs(db: Session):
    return db.query(Blog).all()