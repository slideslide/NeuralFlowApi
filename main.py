from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Http.Routes import router
from Utility.Models.Response import ResponseModel
import pymongo
import CONFIG
app = FastAPI(title="NeuralFlow API",
              version="0.0.1",
              terms_of_service="http://www.neuralflow.com",
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

app.include_router(router,prefix='/api/v1')

