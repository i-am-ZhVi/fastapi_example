from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import FriendPost
from crud import (
    create_friend,
    get_friends
)
from core import db_helper


router = APIRouter(prefix="/friends", tags=["friends"])

@router.get("/")
async def all_friends(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_friends(session)

@router.post("/")
async def new_friend(FriendData: FriendPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_friend(FriendData, session)
