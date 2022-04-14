from typing import List

# from forty.decorators.check_after import check_after

from .base import AbstractController
from ..actions import Commands ,WorkOptions
from ..common import hms_to_time, iso_to_date
from ..views import ActionView, InfoView
from ..models import WorkModel
from ..decorators import check_after


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
            return InfoView("already started")

    @check_after
    def on_finish(self, options: List[str]):
        model = WorkModel(self.pm, self.tm)
        new_time = None
        new_date = None
        if len(options) == 1:
            new_time = hms_to_time(options[0])
        if len(options) == 2:
            new_time = hms_to_time(options[1])
            new_date = iso_to_date(options[0])
        new_action = model.finish(new_date=new_date, new_time=new_time)
        if new_action:
            return ActionView(new_action)
        else:
            return InfoView("already finished")


__all__ = ["WorkController"]
