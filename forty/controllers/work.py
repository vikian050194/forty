from typing import List

# from forty.decorators.check_after import check_after

from .base import AbstractController
from forty.actions import WorkOptions
from forty.common import hms_to_time, iso_to_date
from forty.views import ActionView, InfoView
from forty.models import WorkModel
from forty.decorators import check_after


class WorkController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[WorkOptions.START] = self.on_start
        self.handlers[WorkOptions.FINISH] = self.on_finish

    def on_start(self, options: List[str]):
        model = WorkModel(self.pm, self.tm)
        new_time = None
        new_date = None
        if len(options) == 1:
            new_time = hms_to_time(options[0])
        if len(options) == 2:
            new_time = hms_to_time(options[1])
            new_date = iso_to_date(options[0])
        new_action = model.start(new_date=new_date, new_time=new_time)
        if new_action:
            return ActionView(new_action.type, new_action.value, new_action.timestamp)
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
            return ActionView(new_action.type, new_action.value, new_action.timestamp)
        else:
            return InfoView("already finished")


__all__ = ["WorkController"]
