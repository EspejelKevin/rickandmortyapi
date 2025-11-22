from pydantic import BaseModel
from typing import Any


class Response(BaseModel):
    data: Any
    meta: dict
    status_code: int = 500
