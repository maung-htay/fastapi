from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

class UserBase(BaseModel):
    email: EmailStr    
    
    
class UserCreate(UserBase):
    password: str

class User(UserBase):
   id: int
   created_at: datetime
   
   class Config:
       orm_mode = True 

class PostBase(BaseModel):
   title: str
   content: str
   published: bool = False

class Post(PostBase):
   owner_id: int
   id: int
   created_at: datetime
   owner: User
   
   class Config:
       orm_mode = True
       
class PostOut(BaseModel):
    Post: Post
    votes: int
    
    class Config:
       orm_mode = True
    
class PostCreate(PostBase):
    # owner_id: int
    pass
       
class UserLogin(UserBase):
    password: str       
    
class Token(BaseModel):
    access_token: str
    token_type: str    
    
class TokenData(BaseModel):
    id: Optional[str] = None    

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)    