from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ChatMemberPost
from crud import (
    create_chat_member,
    get_chat_members,
)
from core import db_helper


router = APIRouter(prefix="/chat_members", tags=["chat_members"])

@router.get("/")
async def all_chat_members(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_chat_members(session)

@router.post("/")
async def new_chat_member(ChatMemberData: ChatMemberPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_chat_member(ChatMemberData, session)
