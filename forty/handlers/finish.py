from typing import List

from .base import BaseHandler
from ..actions import Action, Actions


class FinishHandler(BaseHandler):
    @property
    def key(self):
        return Actions.FINISH

    def handle(self, options: List[str]):
        self.pm.load_project()
        actions = self.pm.load_actions()
        if actions and actions[-1].type == Actions.FINISH:
            return
        new_action = Action(Actions.FINISH)
        actions.append(new_action)
        self.pm.save_actions(actions)


__all__ = ["FinishHandler"]
