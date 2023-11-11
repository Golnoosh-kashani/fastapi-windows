from typing import Optional
from pydantic import BaseModel,EmailStr

class User_Create(BaseModel):
    username:str
    email:EmailStr
    password:str
    

class ShowUser(BaseModel):
        username:str
        email:EmailStr
        is_active:bool

        class config():
              orm_mode=True