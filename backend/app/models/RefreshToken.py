from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    token: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))
