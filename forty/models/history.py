from .base import AbstractModel
from ..actions import WorkOptions
from ..reducers import get_dates, get_current_status
from ..reducers.get_today_passed_time import filter_actions


class HistoryModel(AbstractModel):
    def log(self):
        self.pm.load_project()
        actions = self.pm.load_actions()
        return actions

    def date(self):
        self.pm.load_project()
        actions = self.pm.load_actions()
        return get_dates(actions, None).value

    def date_last(self):
        dates = self.date()
        if dates:
            return dates[-1]
        else: None

    def reset(self):
        self.pm.load_project()
        self.pm.save_actions([])

    def undo(self, count = 1):
        self.pm.load_project()
        actions = self.pm.load_actions()
        if actions:
            current_actions_count = len(actions)
            target_actions_delta = count
            if current_actions_count < target_actions_delta:
                target_actions_delta = current_actions_count
            index = 0 - target_actions_delta
            self.pm.save_actions(actions[:index])
            return target_actions_delta
        return 0

    def check(self, day: date):
        self.pm.load_project()
        actions = self.pm.load_actions()
        today_actions = list(filter_actions(actions, day))
        status = get_current_status(today_actions)
        return not status or status.value != WorkOptions.START

    def check_all(self):
        dates = self.date()
        results = []
        for d in dates:
            is_ok = self.check(d)
            if not is_ok:
                results.append((d))
        return results


__all__ = ["HistoryModel"]
