from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Message
from schemas import (
    MessagePost,
    MessageGet,
    ChannelMessagesPost,
    ChatMessagesPost,
)

async def create_message(MessageData: MessagePost, PlaceData: ChannelMessagesPost | ChatMessagesPost , session: AsyncSession):
    new_message = Message(
        userid=MessageData.userid,
        content=MessageData.content
    )

    print("#"*20)
    print(type(PlaceData))
    print("#"*20)

    try:
        session.add(new_message)
        await session.commit()
        return {
            "message": "Сообщение успешно добавленно"
        }
    except:
        return {
            "message": "Не удалось добавить сообщение"
        }


async def get_messages(session: AsyncSession):
    response = await session.execute(select(Message))
    messages = response.scalars().all()

    return [MessageGet.model_validate(message, from_attributes=True) for message in messages]
