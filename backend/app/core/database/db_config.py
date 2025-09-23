from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_ECHO: bool = False

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD} \
        @{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


db_config = ConfigDataBase()
