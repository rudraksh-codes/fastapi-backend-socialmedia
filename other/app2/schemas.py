from pydantic import BaseModel 
from typing import Optional

class BasePost(BaseModel) : 
    title : str 
    content : str 
    published : bool = True

class CreatePost(BasePost) : 
    pass

class UpdatePost(BasePost) :
    pass

class ResponsePost(BasePost) :
    id : int
    class Config:
        from_attributes = True
