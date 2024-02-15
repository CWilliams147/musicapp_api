from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Token(Base):
    access_token: str
    token_type: str

class User(Base):
    username: str