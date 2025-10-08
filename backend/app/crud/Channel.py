
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Channel
from schemas import (
    ChannelPost,
    ChannelGet,
)


async def create_channel(ChannelData: ChannelPost, session: AsyncSession, user_id: int):
    new_channel = Channel(
        name=ChannelData.name,
        description=ChannelData.description,
        creatorid=user_id,
        ispublic=ChannelData.ispublic,
    )

    try:
        session.add(new_channel)
        await session.commit()
        return {
            "message": "Канал успешно добавлен"
        }
    except:
        return {
            "message": "Не удалось добавить канал"
        }

async def get_channels(session: AsyncSession):
    response = await session.execute(select(Channel))
    channels = response.scalars().all()

    return [ChannelGet.model_validate(channel, from_attributes=True) for channel in channels]
