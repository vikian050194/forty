from datetime import datetime

from utils import State, Action, Actions, Time

class RemainedTimeState(State):
    def __init__(self, value=None, is_started=False, start_timestamp=None):
        super().__init__(value)
        self.is_started = is_started
        self.start_timestamp = start_timestamp


def on_init(state: RemainedTimeState, action: Action):
    return RemainedTimeState(action.value)


def on_start(state: RemainedTimeState, action: Action):
    return RemainedTimeState(state.value, True, action.timestamp)


def on_stop(state: RemainedTimeState, action: Action):
    dt = action.timestamp - state.start_timestamp
    dts = dt.seconds
    old_value = Time(state.value).to_seconds()
    new_value = str(Time.from_seconds(old_value-dts))
    return RemainedTimeState(new_value)


handlers = {
    Actions.INIT: on_init,
    Actions.START: on_start,
    Actions.STOP: on_stop
}


def get_remained_time(state, action):
    if state is None:
        state = RemainedTimeState()

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


__all__ = ["get_remained_time"]