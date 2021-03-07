#!/usr/bin/env python3

from sys import argv
from datetime import datetime
from typing import List

from utils import *
from reducers.get_current_status import get_current_status
from reducers.get_remained_time import get_remained_time


def on_help(value):
    print('forty', 'v0.0.0')
    print('help\tget help')
    print('reset\treset actions')
    # print('config\tget or set configuration parameters')
    print('status\tget current status')
    print('get\tget specific value')
    print('start\tstart work')
    print('finish\tfinish work')
    # print('pause\tstart pause')
    # print('resume\tfinish pause')
    # print('break\tstart pause and automatically finish it')


def on_reset(value):
    save_actions([])


def on_status(value):
    actions = load_actions()
    state = get_current_status(actions)
    print(state.value)


def on_start(value):
    actions = load_actions()
    new_action = Action(Actions.START)
    actions.append(new_action)
    save_actions(actions)


def on_finish(value):
    actions = load_actions()
    new_action = Action(Actions.FINISH)
    actions.append(new_action)
    save_actions(actions)


def on_get(value):
    config = load_config()
    actions = load_actions()
    state = get_remained_time(actions, config)
    value = Time.from_seconds(state.value)
    print(value)


handlers = {
    "help": on_help,
    Commands.RESET: on_reset,
    Commands.STATUS: on_status,
    Commands.START: on_start,
    Commands.FINISH: on_finish,
    Commands.GET: on_get
}


def main(args: List[str]):
    command = "help"
    value = None

    if len(args) == 1:
        command = args[0]

    if len(args) == 2:
        value = args[1]

    if command in handlers:
        return handlers[command](value)
    else:
        handlers["help"](value)


if __name__ == "__main__":
    main(argv[1:])
