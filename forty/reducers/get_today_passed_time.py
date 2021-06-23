from typing import List

from ..common import State, to_iso
from ..actions import Action
from . import get_total_passed_time


def filter_actions(actions: List[Action], today: str):
    return filter(lambda action: today in to_iso(action.timestamp), actions)


def get_today_passed_time(actions: List[Action], config):
    filtered_actions = filter_actions(actions, config.today)
    return get_total_passed_time(filtered_actions, config)


__all__ = ["get_today_passed_time"]
