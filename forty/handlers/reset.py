from typing import List

from .base import AbstractHandler
from ..actions import Commands


class ResetHandler(AbstractHandler):
    @property
    def key(self):
        return Commands.RESET

    def handle(self, options: List[str]):
        self.pm.load_project()
        self.pm.save_actions([])


__all__ = ["ResetHandler"]
