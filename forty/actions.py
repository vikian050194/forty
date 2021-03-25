import enum
from datetime import datetime

from .common import to_iso


@enum.unique
class Actions(str, enum.Enum):
    START = "start"
    FINISH = "finish"
    PAUSE = "pause"
    RESUME = "resume"


@enum.unique
class Commands(str, enum.Enum):
    HELP = "help"
    STATUS = "status"
    LOG = "log"
    RESET = "reset"
    PLUS = "plus"
    MINUS = "minus"
    BREAK = "break"
    CONFIG = "config"
    GET = "get"
    UNDO = "undo"
    REDO = "redo"


class Action():
    def __init__(self, type: Actions, timestamp: datetime = datetime.now(), value: str = None):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def to_dict(self):
        return dict(type=self.type, timestamp=to_iso(self.timestamp), value=self.value)
