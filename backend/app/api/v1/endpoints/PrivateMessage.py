


from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession

from core import (
    db_helper,
    auth_helper,
)
from crud import (
    create_private_message,
    get_private_messages
)
from schemas import PrivateMessagePost


router = APIRouter(prefix="/private_messages", tags=["private_messages"])

@router.get("/")
async def all_private_messages(session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await get_private_messages(session, user_id)


@router.post("/")
async def new_private_message(PrivateMessageData: PrivateMessagePost,
    session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)
):
    return await create_private_message(PrivateMessageData, session, user_id)
