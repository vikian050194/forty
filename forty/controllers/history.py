from typing import List

from .base import AbstractController
from ..actions import Commands
from ..views import StrView
from ..models import HistoryModel


class HistoryController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.UNDO] = self.handle_undo
        self.handlers[Commands.RESET] = self.handle_reset

    def handle_undo(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        count = 1
        if options:
            count = int(options[0])
        actual_count = model.undo(count)
        if actual_count == 1:
            message = "last 1 action is deleted"
        else:
            message = f"last {actual_count} actions are deleted"
        return StrView(message)

    def handle_reset(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        model.reset()
        return StrView("all actions are deleted")


__all__ = ["HistoryController"]
