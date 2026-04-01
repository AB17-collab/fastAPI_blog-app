from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import user_service

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(request, db: Session = Depends(get_db)):
    return user_service.register_user(db, request)