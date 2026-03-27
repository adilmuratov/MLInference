from typing import Annotated

from fastapi import Path, APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from .schemas import Request
from . import crud

async def request_by_id(
    request_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Request:
    request = await crud.get_request(session=session, request_id=request_id)
    if request is not None:
        return request

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!"
    )