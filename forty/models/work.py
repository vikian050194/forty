from datetime import time

from .base import AbstractModel
from ..actions import Action, WorkOptions


class WorkModel(AbstractModel):
    def start(self, new_time: time):
        project = self.pm.load_project()
        actions = self.pm.load_actions()

        if actions and actions[-1].type == WorkOptions.START:
            return None

        timestamp = self.tm.get_datetime()

        if new_time:
            timestamp = self.tm.merge_time(new_time)

        new_action = Action(type=WorkOptions.START, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        return new_action

    def finish(self, new_time: time):
        project = self.pm.load_project()
        actions = self.pm.load_actions()

        if actions and actions[-1].type == WorkOptions.FINISH:
            return None

        timestamp = self.tm.get_datetime()

        if new_time:
            timestamp = self.tm.merge_time(new_time)

        new_action = Action(type=WorkOptions.FINISH, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        return new_action


__all__ = ["WorkModel"]
