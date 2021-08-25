from typing import List

from .base import AbstractController
from ..actions import Commands
from ..views import StrView
from ..models import UndoModel

class UndoController(AbstractController):
    @property
    def key(self):
        return Commands.UNDO

    def handle(self, options: List[str]):
        model = UndoModel(self.pm, self.tm)
        count = 1
        if options:
            count = int(options[0])
        actual_count = model.undo(count)
        if actual_count == 1:
            message = "last 1 action is deleted"
        else:
            message = f"last {actual_count} actions are deleted"
        return StrView(message)



__all__ = ["UndoController"]
