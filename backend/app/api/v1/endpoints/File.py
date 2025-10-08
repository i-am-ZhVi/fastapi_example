from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import FilePost
from crud import (
    create_file,
    get_files
)
from core import (
    db_helper,
    auth_helper,
)

router = APIRouter(prefix="/files", tags=["files"])

@router.get("/")
async def all_files(session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await get_files(session, user_id)

@router.post("/")
async def new_file(FileData: FilePost,
    session: AsyncSession = Depends(db_helper.get_db_session),
    user_id: int = Depends(auth_helper.get_current_user)):
    return await create_file(FileData, session, user_id)
