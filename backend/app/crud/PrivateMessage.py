from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import PrivateMessage
from schemas import (
    PrivateMessagePost,
    PrivateMessageGet,
)


async def create_private_message(PrivateMessageData: PrivateMessagePost, session: AsyncSession):
    new_message = PrivateMessage(
        senderid=PrivateMessageData.senderid,
        recipientid=PrivateMessageData.recipientid,
        content=PrivateMessageData.content
    )

    try:
        session.add(new_message)
        await session.commit()
        return {
            "message": "Личное сообщение успешно добавленно"
        }
    except:
        return {
            "message": "Не удалось добавить личное сообщение"
        }


async def get_private_messages(session: AsyncSession):
    response = await session.execute(select(PrivateMessage))
    private_messages = response.scalars().all()

    return [PrivateMessageGet.model_validate(message, from_attributes=True) for message in private_messages]
