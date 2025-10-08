from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import (
    MessagePost,
    ChannelMessagesPost,
    ChatMessagesPost
)
from crud import (
    get_messages,
    create_message
)
from core import (
    db_helper,
    auth_helper,
)

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/")
async def all_messages(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_messages(session)

@router.post("/")
async def new_message(MessageData: MessagePost,
    PlaceData: ChannelMessagesPost | ChatMessagesPost,
    session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await create_message(MessageData, PlaceData, session, user_id)
