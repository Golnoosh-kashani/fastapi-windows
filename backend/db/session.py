from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQLALCHEMY_DATABASE_URL=settings.DATABASE_URL
engine=create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
