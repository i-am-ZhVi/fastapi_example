from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import FriendPost
from crud import (
    create_friend,
    get_friends
)
from core import (
    db_helper,
    auth_helper,
)


router = APIRouter(prefix="/friends", tags=["friends"])

@router.get("/")
async def all_friends(session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await get_friends(session, user_id)

@router.post("/")
async def new_friend(FriendData: FriendPost,
    session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await create_friend(FriendData, session, user_id)
