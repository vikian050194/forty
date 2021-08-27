from forty.views.base import ListView
from typing import List

from .base import AbstractController
from ..actions import Commands, Actions


class HelpController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.HELP] = self.handle_help


    def handle_help(self, options):
        lines = []
        list.append(("forty", "v0.1.0"))
        list.append((Commands.HELP, "get help"))
        list.append((Commands.PROJECT, "TBD"))
        list.append((Commands.GET, "TBD"))
        # list.append((Commands.STATUS, "get status"))
        # list.append((Commands.RESET, "reset actions"))
        # list.append((Commands.PLUS, "plus delta time"))
        # list.append((Commands.MINUS, "minus delta time"))
        # list.append((Commands.BREAK, "start pause and automatically finish it after hh:mm:ss"))
        # list.append((Commands.CONFIG, "get or set configuration parameters"))

        list.append((Actions.START, "start work"))
        list.append((Actions.FINISH, "finish work"))
        # list.append((Actions.PAUSE, "pause work"))
        # list.append((Actions.RESUME, "resume work"))
        return ListView(lines)


__all__ = ["HelpController"]
