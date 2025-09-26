from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base


class Friend(Base):
    __tablename__ = "friends"
    id: Mapped[int] = mapped_column(primary_key=True)
    userid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    friendid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    createdat: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))
