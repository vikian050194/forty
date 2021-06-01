from typing import List

from .base import BaseHandler
from ..actions import Action, Actions, Commands
from ..reducers import *
from ..common import to_hms
from ..send_message import send_message


class GetHandler(BaseHandler):
    @property
    def key(self):
        return Commands.GET

    def handle(self, options: List[str]):
        project_name = self.pm.load_project()
        config = self.pm.load_config()
        actions = self.pm.load_actions()

        status = get_current_status(actions)
        status_value = status.value if status else "none"
        print(status_value)
        status_value = status_value + "ed" if status_value[-1] != "e" else status_value + "d"

        if actions and actions[-1].type != Actions.FINISH:
            actions.append(Action(Actions.FINISH))

        values = [project_name, status_value]

        today_passed_time = get_today_passed_time(actions, config)
        today_passed_time_value = to_hms(today_passed_time.value)
        values.append(today_passed_time_value)
        print(today_passed_time_value)

        if config.day_limit:
            today_remained_time = get_today_remained_time(actions, config)
            today_remained_time_value = to_hms(today_remained_time.value)
            values.append(today_remained_time_value)
            print(today_remained_time_value)

        total_passed_time = get_total_passed_time(actions, config)
        total_passed_time_value = to_hms(total_passed_time.value)
        values.append(total_passed_time_value)
        print(total_passed_time_value)

        if config.total_limit:
            total_remained_time = get_total_remained_time(actions, config)
            total_remained_time_value = to_hms(total_remained_time.value)
            values.append(total_remained_time_value)
            print(total_remained_time_value)

        body = "/".join(values)

        print(body)
        send_message("forty", body)


__all__ = ["GetHandler"]
