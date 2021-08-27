import enum
from datetime import datetime
from typing import Union

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
    # LOG = "log"
    # PLUS = "plus"
    # MINUS = "minus"
    # BREAK = "break"
    # CONFIG = "config"
    UNDO = "undo"
    # REDO = "redo"


ActionType = Union[Actions, Commands]


@enum.unique
class StatusOptions(str, enum.Enum):
    WHATSUP = "whatsup"
    STATUS = "status"
    TODAY = "today"
    TOTAL = "total"
    PASSED = "passed"
    REMAINED = "remained"


@enum.unique
class ProjectOptions(str, enum.Enum):
    LIST = "list"
    NEW = "new"
    GET = "get"
    SET = "set"


class Action():
    def __init__(self, type: Actions, timestamp: datetime, value: str = None):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.type} at {to_iso(self.timestamp)}"

    def __eq__(self, other): 
        if not isinstance(other, Action):
            return NotImplementedError()
        return self.type == other.type and self.timestamp == other.timestamp and self.value == other.value

    def to_dict(self):
        return dict(type=self.type, timestamp=to_iso(self.timestamp), value=self.value)
