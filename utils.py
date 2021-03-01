import json
import subprocess
import enum

from datetime import datetime


filename = "state.json"


@enum.unique
class Actions(str, enum.Enum):
    INIT = "init"
    START = "start"
    STOP = "stop"


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


def actions_applicator(reducer, actions):
    state = None
    for action in actions:
        state = reducer(state, action)
    return state


class State():
    def __init__(self, value=None):
        self.value = value


def load_actions():
    with open(filename, "r") as fr:
        return list(map(make_action, json.load(fr).get("actions")))


def save_actions(actions):
    actions_dict = list(map(lambda item: item.to_dict(), actions))
    data = dict(actions=actions_dict)
    with open(filename, "w") as fw:
        json.dump(data, fw)


def send_message(title, message):
    subprocess.Popen(['notify-send', title, message])
    return

    