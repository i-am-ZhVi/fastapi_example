
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from sqlalchemy.schema import ForeignKey
from models import Base

class ChannelMessages(Base):
    __tablename__ = "channel_messages"
    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id"), primary_key=True, nullable=False)
    message_id: Mapped[int] = mapped_column(ForeignKey("messages.id"), primary_key=True, nullable=False)
