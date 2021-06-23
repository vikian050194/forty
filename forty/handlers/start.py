from typing import List

from .base import AbstractHandler
from ..actions import Action, Actions
from ..common import to_time


class StartHandler(AbstractHandler):
    @property
    def key(self):
        return Actions.START

    def handle(self, options: List[str]):
        project = self.pm.load_project()
        actions = self.pm.load_actions()
        if actions and actions[-1].type == Actions.START:
            self.om.emmit("already started")
            return
        timestamp = self.tm.get_datetime()
        if options:
            new_time = to_time(options[0])
            timestamp = self.tm.merge_time(new_time)
        new_action = Action(type=Actions.START, timestamp=timestamp)
        actions.append(new_action)
        self.pm.save_actions(actions)
        self.om.emmit(str(new_action))


__all__ = ["StartHandler"]
