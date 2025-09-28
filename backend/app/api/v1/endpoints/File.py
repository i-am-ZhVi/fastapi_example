from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import FilePost
from crud import (
    create_file,
    get_files
)
from core import db_helper


router = APIRouter(prefix="/files", tags=["files"])

@router.get("/")
async def all_files(session: AsyncSession = Depends(db_helper.get_db_session)):
    return await get_files(session)

@router.post("/")
async def new_file(FileData: FilePost, session: AsyncSession = Depends(db_helper.get_db_session)):
    return await create_file(FileData, session)
