from datetime import datetime
from pydantic import BaseModel


class ChannelSubscriberPost(BaseModel):
    channelid: int

class ChannelSubscriberGet(ChannelSubscriberPost):
    id: int
    userid: int
    joinedat: datetime
