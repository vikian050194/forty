from datetime import datetime
from utils import State, Action, Actions, Time, actions_reducer, load_config


class RemainedTimeState(State):
    def __init__(self, value=None, is_started=False, start_timestamp=None):
        super().__init__(value)
        self.is_started = is_started
        self.start_timestamp = start_timestamp


def on_start(state: RemainedTimeState, action: Action):
    return RemainedTimeState(state.value, True, action.timestamp)


def on_finish(state: RemainedTimeState, action: Action):
    dt = action.timestamp - state.start_timestamp
    dts = dt.seconds
    old_value = state.value
    new_value = old_value-dts
    return RemainedTimeState(new_value)


handlers = {
    Actions.START: on_start,
    Actions.FINISH: on_finish
}


def get_remained_time_reducer(state, action):
    if state is None:
        state = initial_state

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


def get_remained_time(actions, config):
    initial_state = RemainedTimeState(config.total * config.day * 3600)
    return actions_reducer(get_remained_time_reducer, actions, initial_state)


__all__ = ["get_remained_time"]