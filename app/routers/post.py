from fastapi import Depends,status, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix="/post",
    tags=['Post']
)

#payload: dict = Body(...)
# limit is query param value
# %20 is space
# join 
@router.get("/",response_model=List[schemas.PostOut])
# @router.get("/")
def get_posts(db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user), limit: int = 10,
              skip: int = 0, search: Optional[str] = ""):
   # post = db.query(models.Post).filter(models.Post.owner_id == current_user.id).limit(limit).offset(skip).all()
   post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
   result = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote,
                                       models.Vote.post_id == models.Post.id,
                                       isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
   return result

@router.get("/{id}",response_model=schemas.PostOut)
def get_post_byid(id: int ,db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):
   
   post = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote,
                                       models.Vote.post_id == models.Post.id,
                                       isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
   # post = db.query(models.Post).filter(models.Post.id == id).first()
   
   if not post:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f'Post with id-{id} is not found.')
   # if post.owner_id != current_user.id:
   #    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
   #                        detail=f'Not authorized to perform reqest action')      
   return post

@router.delete("/{id}")
def post_delete(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
   post = db.query(models.Post).filter(models.Post.id == id)
   if not post.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f'Post with id-{id} is not found.')
   if post.first().owner_id != current_user.id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                          detail=f'Not authorized to perform reqest action')   
   post.delete(synchronize_session=False)
   db.commit() 
   return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def post_update(id: int,updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
   post_query = db.query(models.Post).filter(models.Post.id == id)
   post = post_query.first()
   if not post:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f'Post with id-{id} is not found.')
   if post.owner_id != current_user.id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                          detail=f'Not authorized to perform reqest action')
            
   post_query.update(updated_post.dict(), synchronize_session=False)
   db.commit() 
   return post_query.first()
      

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def post_sqlalchemy(post: schemas.PostCreate,db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):
   # new_post = models.Post(title=post.title, content=post.content)
   print("msg -> ", current_user.id)
   # print(**post.dict())
   new_post = models.Post(owner_id = current_user.id, **post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post