from datetime import datetime
from pydantic.main import BaseModel


class ChatPost(BaseModel):
    isgroup: bool
    name: str


class ChatGet(ChatPost):
    id: int
    creatorid: int
    createdat: datetime
