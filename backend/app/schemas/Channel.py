from datetime import datetime
from pydantic import BaseModel


class ChannelPost(BaseModel):
    name: str
    description: str
    creatorid: int
    ispublic: bool

class ChannelGet(ChannelPost):
    id: int
    createdat: datetime
