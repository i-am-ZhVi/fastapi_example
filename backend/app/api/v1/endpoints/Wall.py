from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from schemas import WallPost
from crud import (
get_walls,
create_wall
)


router = APIRouter(prefix="/walls", tags=["walls"])

@router.get("/")
async def all_walls(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_walls(session)


@router.post("/")
async def new_wall(WallData: WallPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_wall(WallData, session)
