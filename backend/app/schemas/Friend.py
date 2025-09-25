

from datetime import datetime
from pydantic import BaseModel


class FriendPost(BaseModel):
    userid: int
    friendid: int
    status: str

class FriendGet(FriendPost):
    id: int
    createdat: datetime
