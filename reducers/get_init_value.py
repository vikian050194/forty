from utils import State


def on_init(state, action):
    return State(action.value)


handlers = {
    "init": on_init
}


def get_init_value(state, action):
    if state is None:
        state = State()

    if action.type in handlers:
        return handlers[action.type](state, action)
    else:
        return state


__all__ = ["get_init_value"]