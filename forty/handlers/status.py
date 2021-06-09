from typing import List

from .base import AbstractHandler
from ..actions import Commands
from ..reducers import get_current_status


class StatusHandler(AbstractHandler):
    @property
    def key(self):
        return Commands.STATUS

    def handle(self, options: List[str]):
        project = self.pm.load_project()
        actions = self.pm.load_actions()
        status = get_current_status(actions)
        self.om.emmit(status.value)


__all__ = ["StatusHandler"]
