from datetime import datetime, timedelta
from typing import List, Union

from .actions import Action, Actions, Commands
from .data import *
from .reducers import *
from .common import to_hms
from .send_message import send_message


def print_option(option: Union[Actions, Commands], hint):
    print(f"{option.value}\t{hint}")


def on_help(value):
    print("forty", "v0.1.0")

    print_option(Actions.START, "start work")
    print_option(Actions.FINISH, "finish work")
    # print_option(Actions.PAUSE, "pause work")
    # print_option(Actions.RESUME, "resume work")
    
    print_option(Commands.HELP, "get help")
    print_option(Commands.STATUS, "get status")
    print_option(Commands.RESET, "reset actions")
    print_option(Commands.PLUS, "plus delta time")
    print_option(Commands.MINUS, "minus delta time")
    # print_option(Commands.BREAK, "start pause and automatically finish it after hh:mm:ss")
    # print_option(Commands.CONFIG, "get or set configuration parameters")
    print_option(Commands.GET, "get specific value")


def on_reset(value):
    save_actions([])


def on_status(value):
    actions = load_actions()
    status = get_current_status(actions)
    print(status.value)


def on_start(value):
    actions = load_actions()
    if actions and actions[-1].type == Actions.START:
        return
    new_action = Action(Actions.START)
    actions.append(new_action)
    save_actions(actions)


def on_finish(value):
    actions = load_actions()
    if actions and actions[-1].type == Actions.FINISH:
        return
    new_action = Action(Actions.FINISH)
    actions.append(new_action)
    save_actions(actions)


def on_plus(value):
    actions = load_actions()
    time = timedelta(seconds=value)
    if not actions:
        return
    last_action = actions[-1]
    last_action.timestamp = last_action.timestamp + time
    save_actions(actions)


def on_minus(value):
    actions = load_actions()
    time = timedelta(seconds=value)
    if not actions:
        return
    last_action = actions[-1]
    last_action.timestamp = last_action.timestamp - time
    save_actions(actions)


def on_get(value):
    config = load_config()
    actions = load_actions()

    status = get_current_status(actions)
    status_value = status.value if status else "none"

    print(status_value)

    if actions and actions[-1].type != Actions.FINISH:
        actions.append(Action(Actions.FINISH))

    today_passed_time = get_today_passed_time(actions, config)
    today_passed_time_value = to_hms(today_passed_time.value)
    print(today_passed_time_value)

    # today_remained_time = get_today_remained_time(actions, config)
    # today_remained_time_value = to_hms(today_remained_time.value)
    today_remained_time = timedelta(hours=config.day) - timedelta(seconds=today_passed_time.value)
    today_remained_time_value = to_hms(today_remained_time.seconds)
    print(today_remained_time_value)

    total_remained_time = get_total_remained_time(actions, config)
    total_remained_time_value = to_hms(total_remained_time.value)
    print(total_remained_time_value)

    send_message("forty", f"{status_value}:{today_passed_time_value}/{today_remained_time_value}/{total_remained_time_value}")


handlers = {
    Actions.START: on_start,
    Actions.FINISH: on_finish,
    Commands.PLUS: on_plus,
    Commands.MINUS: on_minus,
    Commands.HELP: on_help,
    Commands.RESET: on_reset,
    Commands.STATUS: on_status,
    Commands.GET: on_get
}


def main(args: List[str]):
    command = Commands.HELP
    value = None

    if len(args) > 0:
        command = args[0]

    if len(args) > 1:
        value = args[1]

    if command in handlers:
        return handlers[command](value)
    else:
        handlers[Commands.HELP](value)
