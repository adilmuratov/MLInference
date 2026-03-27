from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from .schemas import Request, RequestCreate
from . import crud
from .dependencies import request_by_id
from .mlservice import model_predict

requests_router = APIRouter(tags=["Requests"])

@requests_router.get("/", response_model=list[Request])
async def get_requests(
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_requests(session=session)


@requests_router.post("/", response_model=Request, status_code=status.HTTP_201_CREATED)
async def create_request(
    request_in: RequestCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    request_in.answer = model_predict(
        request_in.model_name,
        request_in.text
    )
    
    return await crud.create_request(session=session, request_in=request_in)


@requests_router.get("/{product_id}/", response_model=Request)
async def get_request(
    request: Request = Depends(request_by_id)
):
    return request


@requests_router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_request(
    request: Request = Depends(request_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> None:
    await crud.delete_request(session=session, request=request)