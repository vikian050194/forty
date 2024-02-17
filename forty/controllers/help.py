from typing import List

from forty.controllers.base import AbstractController
from forty.actions import Commands, WorkOptions
from forty.views.base import ListView, StrView

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
        lines.append((Commands.STATUS, "get status"))
        return ListView(lines)

    def handle_version(self, options: List[str]):
        return StrView("v0.1.0")

    def handle_project(self, options: List[str]):
        return StrView("TODO")
    

__all__ = ["HelpController"]
