from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Http.Routes import router
from Utility.Models.Response import ResponseModel

app = FastAPI(default_response_class=ResponseModel)
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
