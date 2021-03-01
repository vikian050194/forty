#!/usr/bin/env python3

from sys import argv
from datetime import datetime

from utils import *
from reducers.get_remained_time import get_remained_time


remained = lambda actions: actions_applicator(get_remained_time, actions)


def main(args):
    if len(args) == 0:
        args = ['-h']

    [arg] = args
    if arg in ['-h', '--help']:
        print('fourty', 'v0.0.0')
        print('-h, --help\tget full available info')
        print('-i, --init\tinitialization')
        print('-s, --start\tappend "start" action')
        print('-f, --finish\tappend "finish" action')
        return

    actions = load_actions()

    if arg in ['-i', '--init']:
        new_action = Action(Actions.INIT, value="40:00:00")
        save_actions([new_action])

    if arg in ['-s', '--start']:
        new_action = Action(Actions.START)
        actions.append(new_action)
        save_actions(actions)

    if arg in ['-f', '--finish']:
        new_action = Action(Actions.STOP)
        actions.append(new_action)
        save_actions(actions)

    if arg in ['-r', '--remained']:
        if actions[-1].type != Actions.STOP: 
            actions.append(Action(Actions.STOP))
        final_state = remained(actions)
        print(final_state.value)


if __name__ == "__main__":
    main(argv[1:])