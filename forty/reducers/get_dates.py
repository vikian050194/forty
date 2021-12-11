from ..common import State, reduce_actions
from ..actions import Action, WorkOptions


def on_action(state: State, action: Action):
    date = action.timestamp.date()
    dates = [*state.value]
    if not date in dates:
        dates.append(date)
    return State(dates)


controllers = {
    WorkOptions.START: on_action,
    WorkOptions.FINISH: on_action,
}


def get_dates_reducer(state, action):
    if action.type in controllers:
        return controllers[action.type](state, action)
    else:
        return state


def get_dates(actions, config):
    initial_state = State([])
    return reduce_actions(get_dates_reducer, actions, initial_state)


__all__ = ["get_dates"]
