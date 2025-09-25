from pydantic import BaseModel
from datetime import datetime

class UserPost(BaseModel):
    username: str
    email: str
    password: str
    avatarfileid: int | None
    statusmessage: str | None

class UserLogin(BaseModel):
    email_or_username: str
    password: str

class UserGet(BaseModel):
    id: int
    username: str
    avatarfileid: int | None
    statusmessage: str | None
    createdat: datetime
    updatedat: datetime
