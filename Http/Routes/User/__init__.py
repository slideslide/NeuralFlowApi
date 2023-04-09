from fastapi import APIRouter

from Http.Routes.User.Auth import Login
from Http.Routes.User.Auth import Register
import Http.Routes.User.Operation

router = APIRouter()
router.include_router(Operation.router)
router.include_router(Login.router, prefix="/login")
router.include_router(Register.router, prefix="/register")
