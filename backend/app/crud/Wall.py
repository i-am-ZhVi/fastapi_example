
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Wall
from schemas import (
    WallPost,
    WallGet
)


async def create_wall(WallData: WallPost, session: AsyncSession):
    new_wall = Wall(
        userid=WallData.userid,
        content=WallData.content
    )
    try:
        session.add(new_wall)
        await session.commit()
        return {
            "message": "Публикация успешно создана"
        }
    except:
        return {
            "message": "Не удалось создать публикацию"
        }


async def get_walls(session: AsyncSession):
    response = await session.execute(select(Wall))
    walls = response.scalars().all()

    return [WallGet.model_validate(wall, from_attributes=True) for wall in walls]
