
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import File
from schemas import (
    FilePost,
    FileGet,
)


async def create_file(FileData: FilePost, session: AsyncSession, user_id: int):
    new_file = File(
        uploaderid=user_id,
        filename=FileData.filename,
        content=FileData.content,
    )

    try:
        session.add(new_file)
        await session.commit()
        return {
            "message": "Файл успешно добавлен"
        }
    except:
        return {
            "message": "Не удалось добавить файл"
        }

async def get_files(session: AsyncSession, user_id: int):
    response = await session.execute(select(File).where(File.uploaderid == user_id))
    files = response.scalars().all()

    return [FileGet.model_validate(file, from_attributes=True) for file in files]
