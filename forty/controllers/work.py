from typing import List

from .base import AbstractController
from ..actions import Commands ,WorkOptions
from ..common import hms_to_time
from ..views import ActionView, StrView
from ..models import WorkModel


class WorkController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.WORK] = self.handle_subcommand

    def handle_subcommand(self, options: List[str]):
        subhandlers = {
            WorkOptions.START: self.on_start,
            WorkOptions.FINISH: self.on_finish
        }

        command = None
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in subhandlers:
            return subhandlers[command](args)

    def on_start(self, options: List[str]):
        model = WorkModel(self.pm, self.tm)
        new_time = hms_to_time(options[0]) if options else None
        new_action = model.start(new_time)
        if new_action:
            return ActionView(new_action)
        else:
            return StrView("already started")

    def on_finish(self, options: List[str]):
        model = WorkModel(self.pm, self.tm)
        new_time = hms_to_time(options[0]) if options else None
        new_action = model.finish(new_time)
        if new_action:
            return ActionView(new_action)
        else:
            return StrView("already finished")


__all__ = ["WorkController"]
