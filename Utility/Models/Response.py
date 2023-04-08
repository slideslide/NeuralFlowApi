from typing import Any

from fastapi import FastAPI, Response
import orjson
from Utility.Models.HttpStatus import HttpStatus


class ResponseModel(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return orjson.dumps(
            {
                "code": self.status_code,
                "message": HttpStatus.get_message(self.status_code),
                "data": content
            },
            option=orjson.OPT_INDENT_2)
