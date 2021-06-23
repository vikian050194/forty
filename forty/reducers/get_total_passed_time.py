from ..common import State, actions_reducer
from ..actions import Action, Actions


class PassedTimeState(State):
    def __init__(self, value=None, is_started=False, start_timestamp=None):
        super().__init__(value)
        self.is_started = is_started
        self.start_timestamp = start_timestamp


def on_start(state: PassedTimeState, action: Action):
    return PassedTimeState(state.value, True, action.timestamp)


def on_finish(state: PassedTimeState, action: Action):
    dt = action.timestamp - state.start_timestamp
    dts = dt.seconds + 24 * 60 * 60 * dt.days
    old_value = state.value
    new_value = old_value + dts
    return PassedTimeState(new_value)


handlers = {
    Actions.START: on_start,
    Actions.FINISH: on_finish
}


def get_total_passed_time_reducer(state, action):
    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


def get_total_passed_time(actions, config):
    initial_state = PassedTimeState(0)
    return actions_reducer(get_total_passed_time_reducer, actions, initial_state)


__all__ = ["get_total_passed_time"]