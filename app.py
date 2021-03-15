#!/usr/bin/env python3

from sys import argv
from datetime import datetime, timedelta
from typing import List, Union

from utils import *
from reducers.get_current_status import get_current_status
from reducers.get_remained_time import get_remained_time


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
    state = get_current_status(actions)
    print(state.value)


def on_start(value):
    actions = load_actions()
    if actions[-1].type == Actions.START:
        return
    new_action = Action(Actions.START)
    actions.append(new_action)
    save_actions(actions)


def on_finish(value):
    actions = load_actions()
    if actions[-1].type == Actions.FINISH:
        return
    new_action = Action(Actions.FINISH)
    actions.append(new_action)
    save_actions(actions)


def on_plus(value):
    actions = load_actions()
    time = Time(value)
    last_action = actions[-1]
    last_action.timestamp = last_action.timestamp + time.to_timedelta()
    save_actions(actions)


def on_minus(value):
    actions = load_actions()
    time = Time(value)
    last_action = actions[-1]
    last_action.timestamp = last_action.timestamp - time.to_timedelta()
    save_actions(actions)


def on_get(value):
    config = load_config()
    actions = load_actions()
    if actions[-1].type != Actions.FINISH:
        actions.append(Action(Actions.FINISH))
    state = get_remained_time(actions, config)
    value = Time.from_seconds(state.value)
    print(value)
    send_message("forty", str(value))


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


if __name__ == "__main__":
    main(argv[1:])
