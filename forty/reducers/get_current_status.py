from datetime import datetime

from ..common import State, actions_reducer
from ..actions import Action, Actions


def on_action(state: State, action: Action):
    return State(action.type)


handlers = {
    Actions.START: on_action,
    Actions.FINISH: on_action,
}


def get_current_status_reducer(state, action):
    if state is None:
        state = State()

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


def get_current_status(actions):
    return actions_reducer(get_current_status_reducer, actions)


__all__ = ["get_current_status"]
