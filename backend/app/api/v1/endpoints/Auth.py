from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from core import db_helper, settings
from utils import (
    create_access_token,
    create_refresh_token,
    decode_token,
)

from models import (
    User,
    RefreshToken,
)
from schemas import (
    UserLogin,
    TokenPair,
    TokenRefresh,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenPair)
async def login(response: Response, user_in: UserLogin, db: AsyncSession = Depends(db_helper.get_db_session)):
    query = select(User).where(User.email == user_in.email_or_username
        or User.username == user_in.email_or_username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user or not settings.pwd_context.verify(user_in.password, user.passwordhash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверные данные")

    data = {
        "id": str(user.id),
        "Role": str(user.role),
    }
    access = create_access_token(data)
    refresh = create_refresh_token(data)

    # сохраняем refresh в базу (при желании можно хранить несколько)
    db.add(RefreshToken(user_id=user.id, token=refresh))
    await db.commit()

    response.set_cookie(
        key=settings.COOKIES_NAME,
        value=access,
        httponly=True,
        secure=False,
    )

    return TokenPair(access_token=access, refresh_token=refresh)


@router.post("/refresh", response_model=TokenPair)
async def refresh_tokens(data: TokenRefresh, db: AsyncSession = Depends(db_helper.get_db_session)):
    try:
        payload = decode_token(data.refresh_token)
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Неверный тип токена")
    except Exception:
        raise HTTPException(status_code=401, detail="Невалидный refresh токен")

    # проверяем, что токен есть в базе
    query = select(RefreshToken).where(RefreshToken.token == data.refresh_token)
    result = await db.execute(query)
    stored = result.scalar_one_or_none()

    if not stored:
        raise HTTPException(status_code=401, detail="Refresh токен отозван")

    user_id = int(payload["sub"])

    # 👉 можно сделать "одноразовый refresh": удалить старый и выдать новый
    await db.execute(delete(RefreshToken).where(RefreshToken.token == data.refresh_token))
    await db.commit()

    access = create_access_token({"sub": str(user_id)})
    new_refresh = create_refresh_token({"sub": str(user_id)})

    db.add(RefreshToken(user_id=user_id, token=new_refresh))
    await db.commit()

    return TokenPair(access_token=access, refresh_token=new_refresh)
