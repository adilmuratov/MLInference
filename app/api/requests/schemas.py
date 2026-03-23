from pydantic import BaseModel, ConfigDict

class RequestBase(BaseModel):
    model_name: str
    text: str
    answer: bool


class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    model_config = ConfigDict(from_attributes=True)

    id: int