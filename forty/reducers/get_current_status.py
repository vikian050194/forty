from ..common import State, reduce_actions
from ..actions import Action, Actions


def on_action(state: State, action: Action):
    return State(action.type)


controllers = {
    Actions.START: on_action,
    Actions.FINISH: on_action,
}


def get_current_status_reducer(state, action):
    if state is None:
        state = State()

    if action.type in controllers:
        return controllers[action.type](state, action)
    else:
        return state


def get_current_status(actions):
    return reduce_actions(get_current_status_reducer, actions)


__all__ = ["get_current_status"]
