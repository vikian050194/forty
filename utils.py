import json
import subprocess
import enum

from datetime import datetime, timedelta

dir = "/home/kirill/git/forty/"
file_config = dir + "config.json"
file_actions = dir + "actions.json"


class Config():
    def __init__(self, total: int, day: int):
        self.total = total
        self.day = day

    def to_dict(self):
        return {
            "total": self.total,
            "day": self.day
        }


def load_config() -> Config:
    with open(file_config, "r") as fr:
        values = json.load(fr)
        return Config(values["total"], values["day"])


def save_config(config: Config):
    with open(file_config, "w") as fw:
        json.dump(config.to_dict(), fw)



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

# datetime.fromisoformat('2011-11-04T00:05:23')
# datetime.now().isoformat(sep='T', timespec='seconds')
# t1 = datetime.fromisoformat('2011-11-04T00:05:23')
# t2 = datetime.fromisoformat('2011-11-04T00:06:23')
# dt = t2 - t1


def to_iso(value: datetime):
    return value.isoformat(sep='T', timespec='seconds')


def from_iso(value: str):
    return datetime.fromisoformat(value)


class Time():
    def __init__(self, value):
        [h, m, s] = value.split(':')
        self.hours = int(h)
        self.minutes = int(m)
        self.seconds = int(s)

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def from_seconds(value: int):
        h = int(value/3600)
        m = int((value/60)%60)
        s = int(value%60)
        return Time(f'{h}:{m}:{s}')

    def to_seconds(self):
        return self.hours*3600 + self.minutes*60 + self.seconds

    def to_timedelta(self):
        return timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)

class Action():
    def __init__(self, type: Actions, timestamp: datetime = datetime.now(), value: str = None):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def to_dict(self):
        return dict(
            type=self.type,
            timestamp=self.timestamp.isoformat(sep='T', timespec='seconds'),
            value=self.value
        )


def make_action(data):
    type = data.get("type")
    value = data.get("value")
    timestamp = datetime.fromisoformat(data.get("timestamp"))
    return Action(type, timestamp, value)


def actions_reducer(reducer, actions, initial_state = None):
    state = initial_state
    for action in actions:
        state = reducer(state, action)
    return state


class State():
    def __init__(self, value=None):
        self.value = value


def load_actions():
    with open(file_actions, "r") as fr:
        return list(map(make_action, json.load(fr)))


def save_actions(actions):
    data = list(map(lambda item: item.to_dict(), actions))
    with open(file_actions, "w") as fw:
        json.dump(data, fw)


@enum.unique
class UrgencyLevel(str, enum.Enum):
    LOW = "low"
    NORMAL = "normal"
    CRITICAL = "critical"


def send_message(title, body, expire_time: int = 10):
    urgency: UrgencyLevel = UrgencyLevel.NORMAL
    icon = dir + "icon48.png"
    arguments = ['notify-send', title, body]
    arguments.append(f"--expire-time={expire_time * 1000}")
    arguments.append(f"--urgency={urgency}")
    arguments.append(f"--icon={icon}")
    arguments.append("--hint=int:transient:1")
    # arguments.append("--app-name=forty")
    subprocess.Popen(arguments)
