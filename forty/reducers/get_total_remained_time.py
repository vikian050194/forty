from datetime import timedelta
from forty.common import State
from forty.managers.file_manager import Config

from forty.reducers import get_total_passed_time


def get_total_remained_time(actions, config: Config):
    total_passed_time = get_total_passed_time(actions, config)
    value = config.total_limit * int(timedelta(hours=1).total_seconds()) - total_passed_time.value
    state = State(value)
    return state


__all__ = ["get_total_remained_time"]
