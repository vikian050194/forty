from datetime import datetime

from forty.common import Time, State, actions_reducer
from forty.actions import Action, Actions


def on_foo(state: State, action: Action):
    return State(action.type)


handlers = {
    Actions.START: on_foo,
    Actions.FINISH: on_foo,
    Actions.PAUSE: on_foo,
    Actions.RESUME: on_foo
}


def get_current_status_reducer(state, action):
    if state is None:
        state = State()

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


get_current_status = lambda actions: actions_reducer(get_current_status_reducer, actions)


__all__ = ["get_current_status"]