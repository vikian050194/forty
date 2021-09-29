from typing import List

from .base import AbstractController
from ..actions import Actions
from ..common import to_time
from ..views import ActionView, StrView
from ..models import StartModel, FinishModel


class WorkController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Actions.START] = self.handle_start
        self.handlers[Actions.FINISH] = self.handle_finish

    def handle_start(self, options: List[str]):
        model = StartModel(self.pm, self.tm)
        new_time = to_time(options[0]) if options else None
        new_action = model.start(new_time)
        if new_action:
            return ActionView(new_action)
        else:
            return StrView("already started")

    def handle_finish(self, options: List[str]):
        model = FinishModel(self.pm, self.tm)
        new_time = to_time(options[0]) if options else None
        new_action = model.finish(new_time)
        if new_action:
            return ActionView(new_action)
        else:
            return StrView("already finished")


__all__ = ["WorkController"]
