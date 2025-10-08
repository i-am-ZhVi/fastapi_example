from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ChatMemberPost
from crud import (
    create_chat_member,
    get_chat_members,
)
from core import (
    db_helper,
    auth_helper,
)

router = APIRouter(prefix="/chat_members", tags=["chat_members"])

@router.get("/")
async def all_chat_members(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_chat_members(session)

@router.post("/")
async def new_chat_member(ChatMemberData: ChatMemberPost,
    session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await create_chat_member(ChatMemberData, session, user_id)
