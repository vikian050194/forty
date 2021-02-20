from utils import State

class RemainedTimeState(State):
    def __init__(self, value=None, is_started=False, start_timestamp=None):
        super().__init__(value)
        self.is_started = is_started
        self.start_timestamp = start_timestamp


def on_init(state, action):
    return RemainedTimeState(action.value)


def on_start(state, action):
    return RemainedTimeState()


def on_stop(state, action):
    return RemainedTimeState()


handlers = {
    "init": on_init,
    "start": on_start,
    "stop": on_stop
}


def get_remained_time(state, action):
    if state is None:
        state = RemainedTimeState()

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


__all__ = ["get_remained_time"]