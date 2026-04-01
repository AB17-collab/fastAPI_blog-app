from fastapi import FastAPI
from app.models.models import Base
from app.db.session import engine
from app.api import blog, user, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(blog.router)