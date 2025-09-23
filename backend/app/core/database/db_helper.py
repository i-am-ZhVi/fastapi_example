from asyncio import current_task
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import  (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.asyncio.scoping import async_scoped_session
from sqlalchemy import exc

from core.database import db_config


class DataBaseHelper:
    def __init__(self, db_url, db_echo=False):
        self.engine = create_async_engine(url=db_url, echo=db_echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scope_sessions(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )

    @asynccontextmanager
    async def get_db_session(self):
        session = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()


db_helper = DataBaseHelper(db_config.database_url, db_config.DB_ECHO)
