from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated
from datetime import datetime


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = {"from_attributes": True}


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = {"from_attributes": True}


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    model_config = {"from_attributes": True}


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None

# REPLACE with this
class Vote(BaseModel):
    dir: Annotated[int, Field(le=1, ge=0)]