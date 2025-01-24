from pydantic import BaseModel

class Whisper(BaseModel):
    username: str
    content: str
    topic: str