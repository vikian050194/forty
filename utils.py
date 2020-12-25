import json
import subprocess

from time import localtime


filename = "state.json"


class Time():
    def __init__(self, value):
        [h, m, s] = value.split(':')
        self.hours = int(h)
        self.minutes = int(m)
        self.seconds = int(s)

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


def load_state():
    with open(filename, "r") as fr:
        return State(json.load(fr))


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
