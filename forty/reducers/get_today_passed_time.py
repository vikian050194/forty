from typing import List

from datetime import date

from forty.actions import Action
from forty.reducers import get_total_passed_time


def filter_actions(actions: List[Action], today: date):
    return filter(lambda action: today == action.timestamp.date(), actions)


def get_today_passed_time(actions: List[Action], config):
    filtered_actions = filter_actions(actions, config.today)
    return get_total_passed_time(filtered_actions, config)


__all__ = ["get_today_passed_time"]
