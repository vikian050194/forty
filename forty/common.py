import enum
from datetime import datetime, timedelta


def to_iso(value: datetime):
    return value.isoformat(sep='T', timespec='seconds')


def from_iso(value: str):
    return datetime.fromisoformat(value)


def actions_reducer(reducer, actions, initial_state = None):
    state = initial_state
    for action in actions:
        state = reducer(state, action)
    return state


class State():
    def __init__(self, value=None):
        self.value = value


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
