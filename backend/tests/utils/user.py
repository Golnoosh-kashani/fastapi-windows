from sqlalchemy.orm import Session
import random
import string
from schemas.users import User_Create
from db.repository.users import create_new_user
from fastapi.testclient import TestClient
from db.repository import get_user_by_email
from pydantic import EmailStr

def random_lower_string()-> str:
    return "".join(random.choices(string.ascii_lowercase,k=32))
def create_random_owner(db:Session):
    username=random_lower_string()
    email=f"{random_lower_string()}@example.com"
    password=random_lower_string()
    user_schema=User_Create(username=username,email=email,password=password)
    user=create_new_user(user=user_schema,db=db)
    #print(f"User created with ID: {user.id}")
    return user


def user_authentication_headers(client:TestClient,email:EmailStr,password:str):
    data={"email":email,"password":password}
    r=client.post("/login/token",data=data)
    response=r.json()
    auth_token=response["access_token"]
    headers={"Authorization":f"Bearer{auth_token}"}
    return headers




def authentication_token_from_email(username:str,client:TestClient,email:str,db:Session):
    password="randompassword"
    user=get_user_by_email(email=email,db=db)
    if not user:
        user_in_create=User_Create(username=username,email=email,password=password)
        user=create_new_user(user=user_in_create,db=db)
    return user_authentication_headers(client=client,email=email,password=password)    