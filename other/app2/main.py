from fastapi import FastAPI, Depends
import psycopg2 
from psycopg2.extras import RealDictCursor
from fastapi.params import Body

from ...app2 import database
from ...app2 import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session


app = FastAPI() 

models.Base.metadata.create_all(bind = engine)

#postgres connection setup
conn = psycopg2.connect(host = "localhost", password = "2006", user = "postgres", database = "fastapi", cursor_factory=RealDictCursor)
cursor = conn.cursor()



@app.get("/") 
def root() : 
    return {"message" : "this is the root page"}

@app.get("/posts") 
def get_posts(db : Session = Depends(get_db)) : 
    # cursor.execute("""SELECT * FROM posts;""")
    # posts = cursor.fetchall()
    all_posts = db.query(models.Post).all()
    return {"data" : all_posts}

@app.get("/posts/{id}", response_model=schemas.ResponsePost)
def get_post(id : int, db : Session = Depends(get_db)) : 
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post = cursor.fetchone() 
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    return post

@app.post("/posts")
def create_post(post : schemas.CreatePost, db : Session = Depends(get_db)) : 
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) returning * """, (post.title, post.content, post.published, ))
    # created_post = cursor.fetchone()
    # conn.commit()
    created_post = models.Post(**post.model_dump())
    db.add(created_post) 
    db.commit()
    db.refresh(created_post)

    return {"created_post" : created_post}

@app.put("/posts/{id}") 
def update_post(post : schemas.UpdatePost, id : int, db : Session = Depends(get_db)) : 
#     cursor.execute("""update  posts set title = %s, content = %s, published = %s where id = %s returning * ;
# """, (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchall()
    # conn.commit()


    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.update(post.dict() ,synchronize_session=False)
    db.commit()
    return {"updated_post" : post_query.first()}

@app.delete("/posts/{id}") 
def delete_post(id : int) : 
    cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (id, ))
    deleted_post = cursor.fetchone() 
    conn.commit()
    return {"deleted_post" : deleted_post}
    


#remember that - order does matter in writing these endpts.