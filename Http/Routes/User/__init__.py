from fastapi import APIRouter

import Http.Routes.User.Login
import Http.Routes.User.Register

router = APIRouter()
router.include_router(Login.router, prefix="/login")
router.include_router(Register.router, prefix="/register")
@router.get("/")
async def root():
    return "User"