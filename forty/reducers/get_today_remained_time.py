from typing import List

from datetime import timedelta

from forty.common import State
from forty.actions import Action
from forty.managers.project_manager import Config
from forty.reducers import get_today_passed_time


def get_today_remained_time(actions: List[Action], config: Config):
    today_passed_time = get_today_passed_time(actions, config)
    today_remained_time = timedelta(hours=config.day_limit) - timedelta(seconds=today_passed_time.value)
    value = 0
    if today_remained_time.days >= 0:
        value = today_remained_time.seconds
    else:
        value = today_remained_time.seconds + 24 * 60 * 60 * today_remained_time.days
    return State(value)


__all__ = ["get_today_remained_time"]
