from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users import schemas
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import ClassVar, AsyncGenerator

class User(BaseModel, SQLAlchemyBaseUserTable[int]):
    __tablename__: ClassVar[str] = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    role: Mapped[str] = mapped_column(String, default="PATIENT")
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_pwd: Mapped[str] = mapped_column(String, nullable=False)
    is_active_flag: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser_flag: Mapped[bool] = mapped_column(Boolean, default=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email_address": "email_address@example.com"
            }
        }

class UserCreate(BaseModel):
    role: str = "PATIENT"
    username: str
    email_address: str
    password: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email_address": "email_address@example.com",
                "password": "password123"
            }
        }

class UserRead(BaseModel):
    id: int
    role: str
    username: str
    email_address: str
    is_active_flag: bool
    is_superuser_flag: bool

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email_address": "email_address@example.com",
                "role": "PATIENT",
                "is_active_flag": True,
                "is_superuser_flag": False
            }
        }

def get_user_db(session: Session) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    yield SQLAlchemyUserDatabase(session, User)