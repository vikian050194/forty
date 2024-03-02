from typing import List

from forty.controllers.abstract import AbstractController
from forty.actions import Commands
from forty.options import Options
from forty.views.base import AbstractView, StrView


class VersionController(AbstractController):
    def keys(self) -> List[str]:
        return [Commands.VERSION]

    def handle(self, options: Options) -> AbstractView:
        return StrView("v0.4.0")


__all__ = ["VersionController"]
