
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Friend
from schemas import (
    FriendPost,
    FriendGet,
)


async def create_friend(FriendData: FriendPost,
    session: AsyncSession,
    user_id: int):
    new_friend = Friend(
        userid=user_id,
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

async def get_friends(session: AsyncSession, user_id: int):
    response = await session.execute(select(Friend).where(or_(
        Friend.userid == user_id,
        Friend.friendid == user_id,
    )))
    friends = response.scalars().all()

    return [FriendGet.model_validate(friend, from_attributes=True) for friend in friends]
