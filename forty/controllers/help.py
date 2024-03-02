from typing import List

from forty.actions import Commands
from forty.controllers.abstract import AbstractController
from forty.options import Options
from forty.views.base import AbstractView, ListView, StrView


class HelpController(AbstractController):
    def keys(self) -> List[str]:
        return [Commands.HELP]

    def handle(self, options: Options) -> AbstractView:
        lines = []
        lines.append((Commands.HELP, "get help"))
        lines.append((Commands.PROJECT, "manage projects"))
        lines.append((Commands.STATUS, "get status"))
        return ListView(lines)


__all__ = ["HelpController"]
