import enum
from datetime import datetime

from .common import dt_to_iso


@enum.unique
class Commands(str, enum.Enum):
    HELP = "help"
    VERSION = "version"
    PROJECT = "project"
    LOG = "log"
    # PLUS = "plus"
    # MINUS = "minus"
    # BREAK = "break"
    # CONFIG = "config"
    STATUS = "status"
    HISTORY = "history"
    WORK = "work"

@enum.unique
class WorkOptions(str, enum.Enum):
    START = "start"
    FINISH = "finish"
    # PAUSE = "pause"
    # RESUME = "resume"


@enum.unique
class StatusOptions(str, enum.Enum):
    WHATSUP = "whatsup"
    ONLY = "only"
    TODAY = "today"
    TOTAL = "total"
    PASSED = "passed"
    REMAINED = "remained"
    INTERVAL = "interval"


@enum.unique
class ProjectOptions(str, enum.Enum):
    LIST = "list"
    NEW = "new"
    GET = "get"
    SET = "set"


@enum.unique
class HistoryOptions(str, enum.Enum):
    RESET = "reset"
    UNDO = "undo"
    # REDO = "redo"


class Action():
    def __init__(self, type: WorkOptions, timestamp: datetime, value: str = None):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def __eq__(self, other): 
        if not isinstance(other, Action):
            return NotImplementedError()
        return self.type == other.type and self.timestamp == other.timestamp and self.value == other.value

    def to_dict(self):
        return dict(type=self.type, timestamp=dt_to_iso(self.timestamp), value=self.value)
