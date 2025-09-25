from datetime import datetime
from pydantic import BaseModel


class ChannelSubscriberPost(BaseModel):
    channelid: int
    userid: int

class ChannelSubscriberGet(ChannelSubscriberPost):
    id: int
    joinedat: datetime
