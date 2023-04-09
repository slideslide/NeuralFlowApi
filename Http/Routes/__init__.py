from fastapi import APIRouter
import json
from requests import get
import Http.Routes.User

router = APIRouter()
router.include_router(User.router, prefix="/user", tags=["User"])


@router.get("/", tags=["Index"])
async def index():
    return json.loads(get("https://dxs.moe.gov.cn/zx/json/xl/xlwk/").content.decode('utf-8', 'ignore'))[0]
