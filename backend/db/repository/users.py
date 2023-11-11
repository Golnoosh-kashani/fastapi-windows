from sqlalchemy.orm import session

from schemas.users import User_Create
from db.models.users import User
from core.hashing import hasher


def create_new_user(user:User_Create,db:session):
    user=User(username=user.username,email=user.email,hashed_password=hasher.get_password_hash(user.password),is_active=True,is_superuser=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


