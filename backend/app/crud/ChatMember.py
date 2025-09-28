
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import ChatMember
from schemas import (
    ChatMemberPost,
    ChatMemberGet,
)


async def create_chat_member(ChatMemberData: ChatMemberPost, session: AsyncSession):
    new_file = ChatMember(
        chatid=ChatMemberData.chatid,
        userid=ChatMemberData.userid
    )

    try:
        session.add(new_file)
        await session.commit()
        return {
            "message": "Участник успешно добавлен"
        }
    except:
        return {
            "message": "Не удалось добавить участника"
        }

async def get_chat_members(session: AsyncSession):
    response = await session.execute(select(ChatMember))
    chat_members = response.scalars().all()

    return [ChatMemberGet.model_validate(chat_member, from_attributes=True) for chat_member in chat_members]
