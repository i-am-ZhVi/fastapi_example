from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import (
    Message,
    ChatMessages,
    ChannelMessages,
)
from schemas import (
    MessagePost,
    MessageGet,
    ChannelMessagesPost,
    ChatMessagesPost,
)

async def create_message(MessageData: MessagePost,
    PlaceData: ChannelMessagesPost | ChatMessagesPost ,
    session: AsyncSession,
    user_id: int):

    new_message = Message(
        userid=user_id,
        content=MessageData.content
    )

    try:
        session.add(new_message)
        await session.commit()
        await session.refresh(new_message)

        if (type(PlaceData) == ChannelMessagesPost):
            new_channel_message = ChannelMessages(
                channel_id=PlaceData.channel_id,
                message_id=new_message.id,
            )
            session.add(new_channel_message)
            await session.commit()
        else:
            new_chat_message = ChatMessages(
                chat_id=PlaceData.chat_id,
                message_id=new_message.id,
            )
            session.add(new_chat_message)
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
