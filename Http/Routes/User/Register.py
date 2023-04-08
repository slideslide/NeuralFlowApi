from fastapi import APIRouter

from Utility.MongoDB import UsersDB
from Utility.Models.User import UserModel

router = APIRouter()


@router.post("/")
async def Register(user: UserModel):
    result = UsersDB.insert_one(user.dict())
    return str(result.inserted_id)
