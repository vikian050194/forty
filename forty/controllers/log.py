from typing import List

from .base import AbstractController
from ..actions import Commands
from ..views import LogView


class LogController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.LOG] = self.handle_log

    def handle_log(self, options: List[str]):
        self.pm.load_project()
        actions = self.pm.load_actions()
        return LogView(actions)


__all__ = ["LogController"]
