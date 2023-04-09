import json

from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from orjson import orjson
from starlette import status
from starlette.responses import PlainTextResponse, JSONResponse

from Http.Routes import router
from Utility.Models.HttpStatus import HttpStatus
from Utility.Models.Response import ResponseModel
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import pymongo
import CONFIG

app = FastAPI(title="NeuralFlow API",
              version="0.0.1",
              terms_of_service="https://www.neuralflow.com",
              contact={
                  "name": "Jonyan Dunh",
                  "email": "jonyandunh@outlook.com",
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              default_response_class=ResponseModel
              )
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


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": HttpStatus.get_message(status.HTTP_500_INTERNAL_SERVER_ERROR),
            "data": "An unexpected error occurred: {}".format(exc)
        }),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({
            "code": exc.status_code,
            "message": HttpStatus.get_message(exc.status_code),
            "data": exc.detail
        }),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": HttpStatus.get_message(status.HTTP_422_UNPROCESSABLE_ENTITY),
            "data": {"body": exc.body, "detail": exc.errors()}
        }),
    )


app.include_router(router, prefix='/api/v1')
