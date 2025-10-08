from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from models import PrivateMessage
from schemas import (
    PrivateMessagePost,
    PrivateMessageGet,
)


async def create_private_message(PrivateMessageData: PrivateMessagePost, session: AsyncSession, user_id: int):
    new_message = PrivateMessage(
        senderid=user_id,
        recipientid=PrivateMessageData.recipientid,
        content=PrivateMessageData.content
    )

    try:
        session.add(new_message)
        await session.commit()
        return {
            "message": "Личное сообщение успешно добавленно"
        }
    except Exception as ex:
        print(ex)
        return {
            "message": "Не удалось добавить личное сообщение"
        }


async def get_private_messages(session: AsyncSession, user_id: int):
    response = await session.execute(select(PrivateMessage).where(or_(
        PrivateMessage.senderid == user_id,
        PrivateMessage.recipientid == user_id
    )))
    private_messages = response.scalars().all()

    return [PrivateMessageGet.model_validate(message, from_attributes=True) for message in private_messages]
