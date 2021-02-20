import json
import subprocess

from datetime import datetime


filename = "state.json"


# datetime.fromisoformat('2011-11-04T00:05:23')
# datetime.now().isoformat(sep='T', timespec='seconds')
# t1 = datetime.fromisoformat('2011-11-04T00:05:23')
# t2 = datetime.fromisoformat('2011-11-04T00:06:23')
# dt = t2 - t1


class Time():
    def __init__(self, value):
        [h, m, s] = value.split(':')
        self.hours = int(h)
        self.minutes = int(m)
        self.seconds = int(s)

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


class Action():
    def __init__(self, type, timestamp = datetime.now().isoformat(sep='T', timespec='seconds'), value = None):
        self.type = type
        self.value = value
        self.timestamp = timestamp

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


def make_action(data):
    type = data.get("type")
    value = data.get("value")
    timestamp = datetime.fromisoformat(data.get("timestamp"))
    return Action(type, value, timestamp)


class State():
    def __init__(self, value=None):
        self.value = value


def load_actions():
    with open(filename, "r") as fr:
        return list(map(make_action, json.load(fr).get("actions")))


def save_state(state):
    data = dict(
        hours=state.hours,
        minutes=state.minutes,
        seconds=state.seconds
    )
    with open(filename, "w") as fw:
        json.dump(data, fw)


def send_message(title, message):
    subprocess.Popen(['notify-send', title, message])
    return

    