from fastapi import Query
from pydantic import BaseModel
from typing import Annotated

class UserModel(BaseModel):
    username: str
    password: str
    phone: Annotated[str, Query(min_length=11,max_length=11)]
