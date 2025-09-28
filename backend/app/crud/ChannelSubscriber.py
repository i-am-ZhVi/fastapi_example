
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import ChannelSubscriber
from schemas import (
    ChannelSubscriberPost,
    ChannelSubscriberGet,
)


async def create_channel_subscriber(ChannelSubscriberData: ChannelSubscriberPost, session: AsyncSession):
    new_channel_subscriber = ChannelSubscriber(
        channelid=ChannelSubscriberData.channelid,
        userid=ChannelSubscriberData.userid,
    )

    try:
        session.add(new_channel_subscriber)
        await session.commit()
        return {
            "message": "Подписчик успешно добавлен"
        }
    except:
        return {
            "message": "Не удалось добавить подписчика"
        }

async def get_channel_subscribers(session: AsyncSession):
    response = await session.execute(select(ChannelSubscriber))
    channel_subscribers = response.scalars().all()

    return [ChannelSubscriberGet.model_validate(channel_subscriber, from_attributes=True) for channel_subscriber in channel_subscribers]
