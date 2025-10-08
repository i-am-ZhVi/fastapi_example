from datetime import datetime
from pydantic import BaseModel


class ChannelPost(BaseModel):
    name: str
    description: str
    ispublic: bool

class ChannelGet(ChannelPost):
    id: int
    creatorid: int
    createdat: datetime
