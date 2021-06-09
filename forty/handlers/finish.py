from typing import List

from .base import AbstractHandler
from ..actions import Action, Actions
from ..common import to_time


class FinishHandler(AbstractHandler):
    @property
    def key(self):
        return Actions.FINISH

    def handle(self, options: List[str]):
        project = self.pm.load_project()
        actions = self.pm.load_actions()
        if actions and actions[-1].type == Actions.FINISH:
            return
        timestamp = self.tm.get_datetime()
        if options:
            new_time = to_time(options[0])
            timestamp = self.tm.merge_time(new_time)
        new_action = Action(type=Actions.FINISH, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        self.om.emmit(new_action)


__all__ = ["FinishHandler"]
