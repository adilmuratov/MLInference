from fastapi import FastAPI
import uvicorn

from api.requests.controller import requests_router

app = FastAPI()

app.include_router(router=requests_router, prefix="/requests")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)