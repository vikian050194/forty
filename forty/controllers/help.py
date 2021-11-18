from typing import List

from .base import AbstractController
from ..actions import Commands, Actions, StatusOptions
from ..views.base import ListView, StrView

class HelpController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.HELP] = self.handle_help
        self.handlers[Commands.VERSION] = self.handle_version
        # self.handlers[Commands.PROJECT] = self.handle_project

    def handle_help(self, options: List[str]):
        lines = []
        lines.append((Commands.HELP, "get help"))
        lines.append((Commands.PROJECT, "manage projects"))
        lines.append((Commands.RESET, "reset actions"))
        # lines.append((StatusOptions.STATUS, "get status"))
        # lines.append((Commands.PLUS, "plus delta time"))
        # lines.append((Commands.MINUS, "minus delta time"))
        # lines.append((Commands.BREAK, "start pause and automatically finish it after hh:mm:ss"))
        # lines.append((Commands.CONFIG, "get or set configuration parameters"))

        lines.append((Actions.START, "start work"))
        lines.append((Actions.FINISH, "finish work"))
        # lines.append((Actions.PAUSE, "pause work"))
        # lines.append((Actions.RESUME, "resume work"))
        return ListView(lines)

    def handle_version(self, options: List[str]):
        return StrView("v0.1.0")

    def handle_project(self, options: List[str]):
        return StrView("TODO")
    

__all__ = ["HelpController"]
