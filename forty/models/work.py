from datetime import time, date

from .base import AbstractModel
from ..actions import Action, WorkOptions


class WorkModel(AbstractModel):
    def start(self, new_date: date = None, new_time: time = None):
        project = self.pm.load_project()
        actions = self.pm.load_actions()

        if actions and actions[-1].type == WorkOptions.START:
            return None

        timestamp = self.tm.get_datetime()

        if new_time and not new_date:
            timestamp = self.tm.merge_time(new_time)
        if not new_time and new_date:
            timestamp = self.tm.merge_date(new_date)
        if new_time and new_date:
            timestamp = self.tm.merge_date_time(date=new_date, time=new_time)

        new_action = Action(type=WorkOptions.START, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        return new_action

    def finish(self, new_date: date = None, new_time: time = None):
        project = self.pm.load_project()
        actions = self.pm.load_actions()

        if not actions or (actions and actions[-1].type == WorkOptions.FINISH):
            return None

        timestamp = self.tm.get_datetime()

        if new_time and not new_date:
            timestamp = self.tm.merge_time(new_time)
        if not new_time and new_date:
            timestamp = self.tm.merge_date(new_date)
        if new_time and new_date:
            timestamp = self.tm.merge_date_time(date=new_date, time=new_time)

        new_action = Action(type=WorkOptions.FINISH, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        return new_action


__all__ = ["WorkModel"]
