from datetime import time

from .base import AbstractModel
from ..actions import Action, Actions


class FinishModel(AbstractModel):
    def finish(self, new_time: time):
        project = self.pm.load_project()
        actions = self.pm.load_actions()

        if actions and actions[-1].type == Actions.FINISH:
            return None

        timestamp = self.tm.get_datetime()

        if new_time:
            timestamp = self.tm.merge_time(new_time)

        new_action = Action(type=Actions.FINISH, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        return new_action


__all__ = ["FinishModel"]
