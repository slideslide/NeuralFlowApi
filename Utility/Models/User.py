from fastapi import Query
from pydantic import BaseModel, Required
from typing import Annotated


class UserModel(BaseModel):
    id: str | None = None
    username: str | None = None
    phone: str | None = None
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserRegisterModel(UserModel):
    username: str
    password: str
    phone:Annotated[str, Query(min_length=11, max_length=11)] = Required


class UserLoginModel(UserModel):
    username: str
    password: str
