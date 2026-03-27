from pydantic import BaseModel, ConfigDict
from typing import Optional


class RequestBase(BaseModel):
    model_name: str
    text: str
    answer: Optional[bool] = None


class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    model_config = ConfigDict(from_attributes=True)

    id: int