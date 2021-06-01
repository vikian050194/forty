from typing import List

from .base import BaseHandler
from ..actions import Commands


class UndoHandler(BaseHandler):
    @property
    def key(self):
        return Commands.UNDO

    def handle(self, options: List[str]):
        self.pm.load_project()
        actions = self.pm.load_actions()
        if actions:
            self.pm.save_actions(actions[:-1])


__all__ = ["UndoHandler"]
