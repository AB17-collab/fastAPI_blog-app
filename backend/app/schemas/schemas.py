from pydantic import BaseModel
from typing import List, Optional

class BlogCreate(BaseModel):
    title: str
    content: str
    published: bool = True

class BlogOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str