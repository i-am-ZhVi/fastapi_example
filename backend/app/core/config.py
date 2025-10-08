from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from passlib.context import CryptContext

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    COOKIES_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    DEBUG: bool
    CORS_ALLOWED_ORIGINS: str

    pwd_context: CryptContext = CryptContext(schemes = ["bcrypt"], deprecated = "auto")


settings = Settings()
