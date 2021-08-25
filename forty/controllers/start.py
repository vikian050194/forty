from typing import List

from .base import AbstractController
from ..actions import Actions
from ..common import to_time
from ..views import ActionView, StrView
from ..models import StartModel


class StartController(AbstractController):
    @property
    def key(self):
        return Actions.START

    def handle(self, options: List[str]):
        model = StartModel(self.pm, self.tm)
        new_time = to_time(options[0]) if options else None
        new_action = model.start(new_time)
        if new_action:
            return ActionView(new_action)
        else:
            return StrView("already started")


__all__ = ["StartController"]
