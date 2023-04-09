from fastapi import APIRouter, HTTPException
from starlette import status

from Utility import Oauth2
from Utility.Models.User import UserLoginModel


router = APIRouter()


@router.post("/")
async def Login(LoginUser: UserLoginModel):
    if await Oauth2.authenticateUser(LoginUser.username, LoginUser.password):
        access_token = Oauth2.createToken({"sub": LoginUser.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
