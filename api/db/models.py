from typing import Optional
from sqlmodel import Field, SQLModel,Table
from .base import engine



class User(SQLModel,table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

SQLModel.metadata.create_all(engine)
