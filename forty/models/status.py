from .base import AbstractModel
from ..actions import Action, Actions
from ..reducers import *
from ..common import to_hms


class StatusModel(AbstractModel):
    def _magic(self, is_status=False, is_today=False, is_total=False, is_passed=False, is_remained=False):
        project = self.pm.load_project()
        config = self.pm.load_config()
        actions = self.pm.load_actions()

        status = get_current_status(actions)
        status_value = "none"
        if status:
            status_value = status.value

        if actions and actions[-1].type != Actions.FINISH:
            actions.append(Action(Actions.FINISH, self.tm.get_datetime()))

        values = []

        if is_status:
            values.append(status_value)

        if is_today or is_passed:
            today_passed_time = get_today_passed_time(actions, config)
            today_passed_time_value = to_hms(today_passed_time.value)
            values.append(today_passed_time_value)

        if config.day_limit and (is_today or is_remained):
            today_remained_time = get_today_remained_time(actions, config)
            today_remained_time_value = to_hms(today_remained_time.value)
            values.append(today_remained_time_value)

        if is_total or is_passed:
            total_passed_time = get_total_passed_time(actions, config)
            total_passed_time_value = to_hms(total_passed_time.value)
            values.append(total_passed_time_value)

        if config.total_limit and (is_total or is_remained):
            total_remained_time = get_total_remained_time(actions, config)
            total_remained_time_value = to_hms(total_remained_time.value)
            values.append(total_remained_time_value)

        return values

    def all(self):
        return self._magic(is_status=False, is_today=True, is_total=True, is_passed=True, is_remained=True)


    def status(self):
        return self._magic(is_status=True)

    def today(self):
        is_passed = False
        is_remained = False
        # if options:
        #     option = options[0]
        #     is_passed = option == GetOptions.PASSED
        #     is_remained = option == GetOptions.REMAINED
        return self._magic(is_today=True, is_passed=is_passed, is_remained=is_remained)

    def total(self):
        is_passed = False
        is_remained = False
        # if options:
        #     option = options[0]
        #     is_passed = option == GetOptions.PASSED
        #     is_remained = option == GetOptions.REMAINED
        return self._magic(is_total=True, is_passed=is_passed, is_remained=is_remained)

    def passed(self):
        return self._magic(is_passed=True)

    def remained(self):
        return self._magic(is_status=False, is_remained=True)


__all__ = ["StatusModel"]
