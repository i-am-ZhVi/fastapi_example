from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ChannelSubscriberPost
from crud import (
    create_channel_subscriber,
    get_channel_subscribers,
)
from core import db_helper


router = APIRouter(prefix="/channel_subscribers", tags=["channel_subscribers"])

@router.get("/")
async def all_channel_subscribers(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_channel_subscribers(session)

@router.post("/")
async def new_channel_subscriber(ChannelSubscriberData: ChannelSubscriberPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_channel_subscriber(ChannelSubscriberData, session)
