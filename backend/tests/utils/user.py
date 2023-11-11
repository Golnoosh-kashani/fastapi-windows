from sqlalchemy.orm import Session
import random
import string
from schemas.users import User_Create
from db.repository.users import create_new_user
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

