from pydantic import BaseModel


class ChannelMessagesPost(BaseModel):
    channel_id: int
    message_id: int

class ChannelMessagesGet(ChannelMessagesPost):
    pass
