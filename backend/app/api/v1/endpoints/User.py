
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper
from crud import (
get_users,
create_user,
)
from schemas import UserPost


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def all_users(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_users(session)

@router.post("/")
async def new_user(UserData: UserPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_user(UserData, session)
