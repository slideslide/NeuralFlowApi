from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def Login():
    return "Login"