from typing import Annotated

from fastapi import APIRouter, Depends

from Http.Routes.User.Auth import Login
from Http.Routes.User.Auth import Register
from Http.Routes.User.Operation import Index
from Utility import Oauth2

router = APIRouter(dependencies=[Depends(Oauth2.isValidUsers)])
router.include_router(Index.router)

from Utility.Models.User import UserModel


