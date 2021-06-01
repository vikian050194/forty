import enum
from datetime import datetime

from .common import to_iso


@enum.unique
class Actions(str, enum.Enum):
    START = "start"
    FINISH = "finish"
    # PAUSE = "pause"
    # RESUME = "resume"


@enum.unique
class Commands(str, enum.Enum):
    HELP = "help"
    PROJECT = "project"
    GET = "get"
    RESET = "reset"
    UNDO = "undo"
    STATUS = "status"
    # LOG = "log"
    # PLUS = "plus"
    # MINUS = "minus"
    # BREAK = "break"
    # CONFIG = "config"
    # UNDO = "undo"
    # REDO = "redo"


@enum.unique
class GetOptions(str, enum.Enum):
    ALL = "all"
    STATUS = "status"
    TODAY = "today"
    TOTAL = "total"


@enum.unique
class ProjectOptions(str, enum.Enum):
    LIST = "list"
    NEW = "new"
    GET = "get"
    SET = "set"


class Action():
    def __init__(self, type: Actions, timestamp: datetime = datetime.now(), value: str = None):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def to_dict(self):
        return dict(type=self.type, timestamp=to_iso(self.timestamp), value=self.value)
