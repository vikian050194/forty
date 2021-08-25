from typing import List

from .base import AbstractController
from ..actions import Commands
from ..views import StrView
from ..models import ResetModel


class ResetController(AbstractController):
    @property
    def key(self):
        return Commands.RESET

    def handle(self, options: List[str]):
        model = ResetModel(self.pm, self.tm)
        model.reset()
        return StrView("all actions are deleted")


__all__ = ["ResetController"]
