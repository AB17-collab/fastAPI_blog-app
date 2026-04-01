from sqlalchemy.orm import Session
from app.models.models import User

def create_user(db: Session, data):
    user = User(**data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()