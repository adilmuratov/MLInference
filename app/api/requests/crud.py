from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.request import Request
from .schemas import RequestCreate

async def get_requests(
    session: AsyncSession
) -> list[Request]:
    stmt = select(Request).order_by(Request.id)
    result: Result = await session.execute(stmt)
    requests = result.scalars().all()
    return list(requests)


async def get_request(
    session: AsyncSession,
    request_id: int
) -> Optional[Request]:
    return await session.get(Request, request_id)


async def create_request(
    session: AsyncSession,
    request_in: RequestCreate
) -> Request:
    request = Request(**request_in.model_dump())
    session.add(request)
    await session.commit()
    return request


async def delete_request(
    session: AsyncSession,
    request: Request
) -> None:
    await session.delete(request)
    await session.commit()