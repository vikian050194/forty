from typing import List

from .base import AbstractHandler
from ..actions import Action, Actions, Commands, GetOptions
from ..reducers import *
from ..common import to_hms


def magic(pm, om, tm, is_status=False, is_today=False, is_total=False, is_passed=False, is_remained=False):
    project = pm.load_project()
    config = pm.load_config()
    actions = pm.load_actions()

    status = get_current_status(actions)
    status_value = status.value if status else "none"
    # print(status_value)
    status_value = status_value + "ed" if status_value[-1] != "e" else status_value + "d"

    if actions and actions[-1].type != Actions.FINISH:
        actions.append(Action(Actions.FINISH, tm.get_datetime()))

    values = [project]

    if is_status:
        values.append(status_value)

    if is_today or is_passed:
        today_passed_time = get_today_passed_time(actions, config)
        today_passed_time_value = to_hms(today_passed_time.value)
        values.append(today_passed_time_value)
        # print(today_passed_time_value)

    if config.day_limit and (is_today or is_remained):
        today_remained_time = get_today_remained_time(actions, config)
        today_remained_time_value = to_hms(today_remained_time.value)
        values.append(today_remained_time_value)
        # print(today_remained_time_value)

    if is_total or is_passed:
        total_passed_time = get_total_passed_time(actions, config)
        total_passed_time_value = to_hms(total_passed_time.value)
        values.append(total_passed_time_value)
        # print(total_passed_time_value)

    if config.total_limit and (is_total or is_remained):
        total_remained_time = get_total_remained_time(actions, config)
        total_remained_time_value = to_hms(total_remained_time.value)
        values.append(total_remained_time_value)
        # print(total_remained_time_value)

    message = "/".join(values)

    om.emmit(message)

def on_all(pm, om, tm, options):
    magic(pm, om, tm, is_status=True, is_today=True, is_total=True, is_passed=True, is_remained=True)


def on_status(pm, om, tm, options):
    magic(pm, om, tm, is_status=True)

def on_today(pm, om, tm, options):
    is_passed = False
    is_remained = False
    # if options:
    #     option = options[0]
    #     is_passed = option == GetOptions.PASSED
    #     is_remained = option == GetOptions.REMAINED
    magic(pm, om, tm, is_status=True, is_today=True, is_passed=is_passed, is_remained=is_remained)

def on_total(pm, om, tm, options):
    is_passed = False
    is_remained = False
    # if options:
    #     option = options[0]
    #     is_passed = option == GetOptions.PASSED
    #     is_remained = option == GetOptions.REMAINED
    magic(pm, om, tm, is_status=True, is_total=True, is_passed=is_passed, is_remained=is_remained)

def on_passed(pm, om, tm, options):
    magic(pm, om, tm, is_status=True, is_passed=True)

def on_remained(pm, om, tm, options):
    magic(pm, om, tm, is_status=True, is_remained=True)

handlers = {
    GetOptions.ALL: on_all,
    GetOptions.STATUS: on_status,
    GetOptions.TODAY: on_today,
    GetOptions.TOTAL: on_total,
    GetOptions.PASSED: on_passed,
    GetOptions.REMAINED: on_remained
}


class GetHandler(AbstractHandler):
    @property
    def key(self):
        return Commands.GET

    def handle(self, options: List[str]):
        command = GetOptions.ALL
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in handlers:
            handlers[command](self.pm, self.om, self.tm, args)


__all__ = ["GetHandler"]
