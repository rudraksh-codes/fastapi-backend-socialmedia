from fastapi import FastAPI , Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import List
from .. import oauth2
from typing import Optional
from sqlalchemy import func


router = APIRouter(
    prefix="/posts", 
    tags = ["Posts"]
)



@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user), limit : int =10 , skip :int = 0, search : Optional[str] = "") : 
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Vote.post_id
    ).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()


    return results

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse) 

def create_posts(post : schemas.PostCreate, db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)) : 
    # inserting a new post into db 
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING * """, (post.title, post.content, post.published)) #preventing sql injection attack
    # new_post = cursor.fetchone() 

    # conn.commit()
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #actually retrive from db and store in same variable again to simulate RETURNING * like stuff 
    print(new_post)
    return new_post  #this is an object not a dict to be read by pydantic 
#title str, content str



#path order matters
@router.get("/latest")
def get_latest_post() :
    post = my_posts[len(my_posts)-1]
    return post
   


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id : int, response : Response, db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)) :
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    # test_post = cursor.fetchone()
    post = db.query(models.Post, func.count(models.Vote.post_id
    ).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    print(post)

    if not post :
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"post with id : {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} not found")
    return post
    
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) 
def delete_post(id : int, db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)) : 
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id), ))
    # delete_post = cursor.fetchone()
    # print(delete_post)
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first() 
    if post == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id : {id} not found")
    
    if post.owner_id != current_user.id : 
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)





@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PostResponse)
def update_post(id : int,updated_post : schemas.PostBase, current_user : int = Depends(oauth2.get_current_user), db : Session = Depends(get_db)) :
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s where id = %s returning *""", (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first() 

    

    if not post : 
        raise HTTPException(status_code=404, 
                            detail = f"post with id : {id} not found")
    
    if post.owner_id != current_user.id : 
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit() 
    return post

