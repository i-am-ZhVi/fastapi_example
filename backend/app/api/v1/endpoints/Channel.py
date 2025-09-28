from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ChannelPost
from crud import (
    create_channel,
    get_channels,
)
from core import db_helper


router = APIRouter(prefix="/channels", tags=["channels"])

@router.get("/")
async def all_channels(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_channels(session)

@router.post("/")
async def new_channel(ChannelData: ChannelPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_channel(ChannelData, session)
