
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import (
    User,
    Role,
)
from schemas import (
    UserPost,
    UserGet
)
from core import settings


async def create_user(UserData: UserPost, session: AsyncSession):
    if ((await session.execute(select(User).filter(User.username == UserData.username))).first() != None):
        return {
            "message": "Данное имя занято"
        }
    if ((await session.execute(select(User).filter(User.email == UserData.email))).first() != None):
        return {
            "message": "Данная элетронная почта занята"
        }
    try:
        new_user = User(
            username=UserData.username,
            email=UserData.email,
            passwordhash=settings.pwd_context.hash(UserData.password),
            avatarfileid=UserData.avatarfileid,
            role=Role.user,
           statusmessage=UserData.statusmessage
        )
        session.add(new_user)
        await session.commit()

        return {
            "message": "пользователь успешно создан"
        }
    except Exception as ex:
        print(ex)
        return {
            "message": "Возникла непредвиденная ошибка"
        }

async def get_users(session: AsyncSession):
    response = await session.execute(select(User))
    users = response.scalars().all()

    return [UserGet.model_validate(user, from_attributes=True) for user in users]
