from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from sqlalchemy.orm import Session
from db.models.users import User

def get_user(username:str,db:Session):
    user=db.query(User).filter(user.email==username).first()
    return user
