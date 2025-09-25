

from pydantic import BaseModel


class ChatMessagesPost(BaseModel):
    chat_id: int
    message_id: int

class ChatMessagesGet(ChatMessagesPost):
    pass
