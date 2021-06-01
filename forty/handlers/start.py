from typing import List

from .base import BaseHandler
from ..actions import Action, Actions, Commands


class StartHandler(BaseHandler):
    @property
    def key(self):
        return Actions.START

    def handle(self, options: List[str]):
        self.pm.load_project()
        actions = self.pm.load_actions()
        if actions and actions[-1].type == Actions.START:
            return
        new_action = Action(Actions.START)
        actions.append(new_action)
        self.pm.save_actions(actions)


__all__ = ["StartHandler"]
