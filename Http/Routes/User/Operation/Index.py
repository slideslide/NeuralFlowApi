from typing import Annotated

from fastapi import APIRouter, Depends
from Utility import Oauth2

router = APIRouter()

from Utility.Models.User import UserModel



@router.get("/")
async def index():
    return "welcome!"

@router.get("/info")
async def index(current_user: Annotated[UserModel, Depends(Oauth2.getCurrentUser)]):
    return current_user