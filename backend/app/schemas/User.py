from pydantic import BaseModel
from datetime import datetime

class UserPost(BaseModel):
    username: str
    email: str
    passwordhash: str
    avatarfileid: int
    statusmessage: str | None

class UserGet(UserPost):
    id: int
    createdat: datetime
    updatedat: datetime
