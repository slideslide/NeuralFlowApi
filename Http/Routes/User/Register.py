from fastapi import APIRouter

from Utility.MongoDB import UsersDB
from Utility.Models.User import UserModel
from passlib.context import CryptContext
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post("/")
async def Register(user: UserModel):
    user.password=pwd_context.hash(user.password)
    result = UsersDB.insert_one(user.dict())
    return str(result.inserted_id)
