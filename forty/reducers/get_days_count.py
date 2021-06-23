from ..common import State, actions_reducer
from ..actions import Action, Actions
from . import get_dates


def get_days_count(actions, config):
    dates = get_dates(actions, config)
    value = len(dates.value)
    state = State(value)
    return state


__all__ = ["get_days_count"]
