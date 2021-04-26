import enum
from datetime import datetime, timedelta


def to_iso(value: datetime):
    return value.isoformat(sep='T', timespec='seconds')


def from_iso(value: str):
    return datetime.fromisoformat(value)


def to_ymd(value: datetime):
    return f"{value.year:04d}-{value.month:02d}-{value.day:02d}"


def actions_reducer(reducer, actions, initial_state = None):
    state = initial_state
    for action in actions:
        state = reducer(state, action)
    return state


class State():
    def __init__(self, value=None):
        self.value = value


def to_hms(value: int):
    sign = ""
    if value < 0:
        value = -1 * value
        sign = "-"
    hours, remainder = divmod(value, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{sign}{hours:02d}:{minutes:02d}:{seconds:02d}"


def from_hms(value: str):
    [h, m, s] = value.split(':')
    hours = int(h) * 3600
    minutes = int(m) * 60
    seconds = int(s)
    return hours + minutes + seconds
