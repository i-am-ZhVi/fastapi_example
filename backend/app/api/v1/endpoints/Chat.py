from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ChatPost
from crud import (
    create_chat,
    get_chats,
)
from core import (
    db_helper,
    auth_helper
)

router = APIRouter(prefix="/chats", tags=["chats"])

@router.get("/")
async def all_chats(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_chats(session)

@router.post("/")
async def new_chat(ChatData: ChatPost,
    session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await create_chat(ChatData, session, user_id)
