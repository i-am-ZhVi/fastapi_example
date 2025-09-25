from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base


class Channel(Base):
    __tablename__ = "channels"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    creatorid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    ispublic: Mapped[bool] = mapped_column(nullable=False)
    createdat: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))

    creator: Mapped["User"] = relationship(back_populates="channels")
    subscribers: Mapped[list["ChannelSubscriber"]] = relationship(back_populates="channel")
    messages: Mapped[list["Message"]] = relationship(back_populates="channel")
