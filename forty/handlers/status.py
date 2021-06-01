from typing import List

from .base import BaseHandler
from ..actions import Commands
from ..reducers import get_current_status


class StatusHandler(BaseHandler):
    @property
    def key(self):
        return Commands.STATUS

    def handle(self, options: List[str]):
        actions = self.pm.load_actions()
        status = get_current_status(actions)

        print(status.value)


__all__ = ["StatusHandler"]
