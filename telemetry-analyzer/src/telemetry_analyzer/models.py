from datetime import datetime
from pydantic import BaseModel

class LogEntry(BaseModel):
    timestamp: datetime
    service: str
    level: str
    message: str
