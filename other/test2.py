from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() 

class Post(BaseModel) : 
    title : str
    content : str 
    published : bool = True 

class PostResponse(BaseModel) :
    title : str

    class Config : 
        orm_mode = True

@app.post("/posts", response_model=PostResponse) 
def create_post(post : Post) : 
    return post