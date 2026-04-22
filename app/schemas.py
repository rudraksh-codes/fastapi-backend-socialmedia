from pydantic import BaseModel, EmailStr , conint
from typing import Optional
from datetime import datetime

class PostBase(BaseModel) : 
    title : str 
    content : str 
    published : bool = True 

class PostResponse(PostBase):
    id : int
    created_at : datetime
    owner_id : int 
    owner : UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True




class UserOut(BaseModel) :
    id : int
    email : EmailStr
    created_at : datetime
    
    class Config : 
        orm_mode = True 
 

class PostCreate(PostBase) : 
    pass 




class UserCreate(BaseModel) : 
    email : EmailStr
    password : str 

 
class UserLogin(BaseModel) : 
    email : EmailStr
    password : str 

class Token(BaseModel) : 
    access_token : str 
    token_type : str 

class TokenData(BaseModel) : 
    id : Optional[int] = None 

class Vote(BaseModel) : 
    post_id : str
    dir : conint(le= 1)

