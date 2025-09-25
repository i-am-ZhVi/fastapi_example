

from datetime import datetime
from pydantic import BaseModel


class ChatMemberPost(BaseModel):
    chatid: int
    userid: int

class ChatMemberGet(ChatMemberPost):
    id: int
    joinedat: datetime
