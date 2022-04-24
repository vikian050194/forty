from .base import AbstractModel
from ..actions import Action, WorkOptions
from ..reducers import *
from ..reducers.get_today_passed_time import filter_actions
from ..views.status import OnlyStatusView, TodayStatusView, TotalStatusView, PassedStatusView, RemainedStatusView, IntervalStatusView, FullStatusView
from ..common import int_to_timedelta


class StatusModel(AbstractModel):
    def _magic(self, is_status=False, is_today=False, is_total=False, is_passed=False, is_remained=False, is_interval=False):
        project = self.pm.load_project()
        config = self.pm.load_config()
        actions = self.pm.load_actions()

        status = get_current_status(actions)
        status_value: WorkOptions = None
        if status:
            status_value = status.value

        if actions and actions[-1].type != WorkOptions.FINISH:
            actions.append(Action(WorkOptions.FINISH, self.tm.get_datetime()))

        view = FullStatusView()

        if is_status:
            view.status = status_value

        if is_today or is_passed:
            today_passed_time = get_today_passed_time(actions, config)
            view.today_passed_time = int_to_timedelta(today_passed_time.value)

        if config.day_limit and (is_today or is_remained):
            today_remained_time = get_today_remained_time(actions, config)
            view.today_remained_time = int_to_timedelta(today_remained_time.value)

        if is_total or is_passed:
            total_passed_time = get_total_passed_time(actions, config)
            view.total_passed_time = int_to_timedelta(total_passed_time.value)

        if config.total_limit and (is_total or is_remained):
            total_remained_time = get_total_remained_time(actions, config)
            view.total_remained_time = int_to_timedelta(total_remained_time.value)

        if is_interval:
            today_actions = list(filter_actions(actions, config.today))
            if today_actions:
                view.from_time = today_actions[0].timestamp.time()
            if config.day_limit and status_value == WorkOptions.START:
                today_remained_time = get_today_remained_time(actions, config)
                today_remained_timedelta = int_to_timedelta(today_remained_time.value)
                view.to_time = (self.tm.get_datetime() + today_remained_timedelta).time()
                
        return view

    def all(self):
        return self._magic(is_status=True, is_today=True, is_total=True, is_passed=True, is_remained=True, is_interval=True)


    def only(self):
        all_view = self._magic(is_status=True)
        return OnlyStatusView(status=all_view.status)

    def today(self):
        is_passed = False
        is_remained = False
        # if options:
        #     option = options[0]
        #     is_passed = option == GetOptions.PASSED
        #     is_remained = option == GetOptions.REMAINED
        all_view = self._magic(is_today=True, is_passed=is_passed, is_remained=is_remained)
        return TodayStatusView(passed=all_view.today_passed_time, remained=all_view.today_remained_time)

    def total(self):
        is_passed = False
        is_remained = False
        # if options:
        #     option = options[0]
        #     is_passed = option == GetOptions.PASSED
        #     is_remained = option == GetOptions.REMAINED
        all_view = self._magic(is_total=True, is_passed=is_passed, is_remained=is_remained)
        return TotalStatusView(passed=all_view.total_passed_time, remained=all_view.total_remained_time)

    def passed(self):
        all_view = self._magic(is_passed=True)
        return PassedStatusView(today=all_view.today_passed_time, total=all_view.total_passed_time)

    def remained(self):
        all_view = self._magic(is_remained=True)
        return RemainedStatusView(today=all_view.today_remained_time, total=all_view.total_remained_time)

    def interval(self):
        all_view = self._magic(is_interval=True)
        return IntervalStatusView(from_time=all_view.from_time, to_time=all_view.to_time)


__all__ = ["StatusModel"]
