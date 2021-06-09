from ..common import State
from ..managers.project_manager import Config

from . import get_total_passed_time


def get_total_remained_time(actions, config: Config):
    total_passed_time = get_total_passed_time(actions, config)
    value = config.total_limit * 3600 - total_passed_time.value
    state = State(value)
    return state


__all__ = ["get_total_remained_time"]
