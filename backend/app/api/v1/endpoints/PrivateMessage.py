


from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud import (
    create_private_message,
    get_private_messages
)
from schemas import PrivateMessagePost


router = APIRouter(prefix="/private_messages", tags=["private_messages"])

@router.get("/")
async def all_private_messages(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_private_messages(session)


@router.post("/")
async def new_private_message(PrivateMessageData: PrivateMessagePost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_private_message(PrivateMessageData, session)
