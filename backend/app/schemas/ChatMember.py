

from datetime import datetime
from pydantic import BaseModel


class ChatMemberPost(BaseModel):
    chatid: int


class ChatMemberGet(ChatMemberPost):
    id: int
    userid: int
    joinedat: datetime
