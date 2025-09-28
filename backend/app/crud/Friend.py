
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Friend
from schemas import (
    FriendPost,
    FriendGet,
)


async def create_friend(FriendData: FriendPost, session: AsyncSession):
    new_friend = Friend(
        userid=FriendData.userid,
        friendid=FriendData.friendid,
        status=FriendData.status,
    )

    try:
        session.add(new_friend)
        await session.commit()
        return {
            "message": "Друг успешно добавлен"
        }
    except:
        return {
            "message": "Не удалось добавить друга"
        }

async def get_friends(session: AsyncSession):
    response = await session.execute(select(Friend))
    friends = response.scalars().all()

    return [FriendGet.model_validate(friend, from_attributes=True) for friend in friends]
