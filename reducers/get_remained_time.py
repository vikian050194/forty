from datetime import datetime
from utils import State, Action, Actions, Time, actions_applicator


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
    old_value = Time(state.value).to_seconds()
    new_value = str(Time.from_seconds(old_value-dts))
    return RemainedTimeState(new_value)


handlers = {
    Actions.START: on_start,
    Actions.FINISH: on_finish
}


def get_remained_time_reducer(state, action):
    if state is None:
        state = RemainedTimeState()

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


get_remained_time = lambda actions: actions_applicator(get_remained_time_reducer, actions)


__all__ = ["get_remained_time"]