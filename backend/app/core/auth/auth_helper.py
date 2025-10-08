from fastapi import HTTPException, Request, status
from core import settings
from utils import decode_token
from models import Role

class AuthHelper:
    def __init__(self):
        pass

    def get_current_user(self, request: Request):
        token = request.cookies.get(settings.COOKIES_NAME)
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Авторизуйтесь")
        user_data = decode_token(token)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Авторизуйтесь")
        return int(user_data["id"])

    def protected_layer(self, request: Request):
        token = request.cookies.get(settings.COOKIES_NAME)
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Авторизуйтесь")
        user_data = decode_token(token)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Авторизуйтесь")
        if user_data["Role"] != str(Role.admin):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Не достаточно прав для просмотра данного ресурса")
        return int(user_data["id"])


auth_helper = AuthHelper()
