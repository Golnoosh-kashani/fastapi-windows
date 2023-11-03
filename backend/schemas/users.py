from typing import Optional
from pydantic import BaseModel,EmailStr

class User_Create(BaseModel):
    username:str
    email:EmailStr
    password:str
    