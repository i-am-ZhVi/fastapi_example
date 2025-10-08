
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from core import (
    db_helper,
    auth_helper,
)
from crud import (
get_users,
create_user,
)
from schemas import UserPost


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def all_users(request: Request,session: AsyncSession = Depends(db_helper.get_db_session), user_id: int = Depends(auth_helper.protected_layer)):
    return await get_users(session)

@router.post("/")
async def new_user(UserData: UserPost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_user(UserData, session)
