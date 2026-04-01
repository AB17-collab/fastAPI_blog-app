from sqlalchemy.orm import Session
from app.repositories import user_repo
from app.core.security import hash_password

def register_user(db: Session, request):
    data = request.dict()
    data["password"] = hash_password(data["password"])
    return user_repo.create_user(db, data)