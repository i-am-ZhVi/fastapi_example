
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Chat
from schemas import (
    ChatPost,
    ChatGet,
)


async def create_chat(ChatData: ChatPost, session: AsyncSession):
    new_chat = Chat(
        isgroup=ChatData.isgroup,
        name=ChatData.name,
        creatorid=ChatData.creatorid,
    )

    try:
        session.add(new_chat)
        await session.commit()
        return {
            "message": "Чат успешно добавлен"
        }
    except:
        return {
            "message": "Не удалось добавить чат"
        }

async def get_chats(session: AsyncSession):
    response = await session.execute(select(Chat))
    chats = response.scalars().all()

    return [ChatGet.model_validate(chat, from_attributes=True) for chat in chats]
