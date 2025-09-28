from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import MessagePost
from crud import (
    get_messages,
    create_message
)
from core import db_helper


router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("/")
async def all_messages(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_messages(session)

@router.post("/")
async def new_message(MessageData: MessagePost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_message(MessageData, session)
