from typing import List

from .base import AbstractHandler
from ..actions import Commands


class UndoHandler(AbstractHandler):
    @property
    def key(self):
        return Commands.UNDO

    def handle(self, options: List[str]):
        self.pm.load_project()
        actions = self.pm.load_actions()
        if actions:
            count = 1
            message = "last 1 action is deleted"
            if options:
                count = int(options[0])
                message = f"last {count} actions are deleted"
            count = 0 - count
            self.pm.save_actions(actions[:count])
            self.om.emmit(message)



__all__ = ["UndoHandler"]
