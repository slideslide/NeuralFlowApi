import uuid

from fastapi import APIRouter, HTTPException

from Utility.MongoDB import db
from Utility.Models.User import UserRegisterModel
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/")
async def Register(user: UserRegisterModel):
    user.password = pwd_context.hash(user.password)
    user.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'neuralflow.cn'))
    result = await db.users.insert_one(user.dict())
    return str(result.inserted_id)
