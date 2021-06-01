from datetime import datetime

from ..common import State, actions_reducer, to_ymd
from ..actions import Action, Actions


def on_action(state: State, action: Action):
    date = to_ymd(action.timestamp)
    dates = [*state.value]
    if not date in dates:
        dates.append(date)
    return State(dates)


handlers = {
    Actions.START: on_action,
    Actions.FINISH: on_action,
}


def get_dates_reducer(state, action):
    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


def get_dates(actions, config):
    initial_state = State([])
    return actions_reducer(get_dates_reducer, actions, initial_state)


__all__ = ["get_dates"]
