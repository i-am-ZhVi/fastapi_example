from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    passwordhash: Mapped[str] = mapped_column(nullable=False)
    avatarfileid: Mapped[int] = mapped_column(ForeignKey("files.id"), nullable=True)
    statusmessage: Mapped[str] = mapped_column(nullable=True)
    createdat: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))
    updatedat: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())

    chats: Mapped[list["Chat"]] = relationship(back_populates="creator")
    channels: Mapped[list["Channel"]] = relationship(back_populates="creator")
    messages: Mapped[list["Message"]] = relationship(back_populates="sender")
    walls: Mapped[list["Wall"]] = relationship(back_populates="user")
    files: Mapped[list["File"]] = relationship(back_populates="uploader", primaryjoin="User.id == File.uploaderid")
