from fastapi import FastAPI , Response, status, HTTPException, Depends
from fastapi.params import  Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from typing import List
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#creating table if not exists as per sqlalchemy 
# models.Base.metadata.create_all(bind = engine)


origins = ["https://www.google.com", "https://www.youtube.com"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



while True : 
    try : 
        conn = psycopg2.connect(host = "localhost", database = "fastapi", user = "postgres", password = "2006", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('*'*10, "Database connection was successful",'*'*10)
        break
    except Exception as error :
        print("Connecting to Database failed")
        print("Error : ", error)
        time.sleep(2)

my_posts = [{"title" : "title of post 1", "content" : "content of post1", "id" : 1}, {"title" : "fav food", "content" : "i like pizza", "id": 2}]

def find_post(id) :
    for p in my_posts : 
        if p["id"] == id : 
            return p
        
def find_indes_post(id) : 
    for i, p in enumerate(my_posts) : 
        if p["id"] == id : 
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router) 
app.include_router(vote.router)

@app.get("/") 
def root() : 
    return {"message" : "Hello World!!!!"}
    
