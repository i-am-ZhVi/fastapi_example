from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base



class ChannelSubscriber(Base):
    __tablename__ = "channelsubscribers"
    id: Mapped[int] = mapped_column(primary_key=True)
    channelid: Mapped[int] = mapped_column(ForeignKey("channels.id"), nullable=False)
    userid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    joinedat: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))

    channel: Mapped["Channel"] = relationship(back_populates="subscribers")
