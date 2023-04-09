from datetime import timedelta, datetime
from typing import Annotated

from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from Utility.Models.User import UserModel
from Utility.MongoDB import db
from starlette import status

import CONFIG

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60


def createToken(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, CONFIG.SECRET_KEY, algorithm=CONFIG.ALGORITHM)
    return encoded_jwt


async def getCurrentUser(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, CONFIG.SECRET_KEY, algorithms=[CONFIG.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await db.users.find_one({"username": username})
    if user is None:
        raise credentials_exception
    user.pop("_id")
    return UserModel(**user)


async def isValidUsers(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, CONFIG.SECRET_KEY, algorithms=[CONFIG.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await db.users.find_one({"username": username})
    if user is None:
        raise credentials_exception
    if user["disabled"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The account has been disabled!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True


async def authenticateUser(username: str, password: str):
    user = await db.users.find_one({"username": username})
    if not user:
        return False
    if not pwd_context.verify(password, user["password"]):
        return False
    return True
