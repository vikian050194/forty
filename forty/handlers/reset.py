from typing import List

from .base import BaseHandler
from ..actions import Commands


class ResetHandler(BaseHandler):
    @property
    def key(self):
        return Commands.RESET

    def handle(self, options: List[str]):
        self.pm.load_project()
        self.pm.save_actions([])


__all__ = ["ResetHandler"]
