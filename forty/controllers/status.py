from typing import List

from .base import AbstractController
from ..actions import Commands, StatusOptions
from ..reducers import *
from ..models import StatusModel
from ..decorators import check_before


class StatusController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.STATUS] = self.handle_subcommand

    @check_before
    def handle_subcommand(self, options: List[str]):
        subhandlers = {
            StatusOptions.WHATSUP: self.on_whatsup,
            StatusOptions.ONLY: self.on_only,
            StatusOptions.TODAY: self.on_today,
            StatusOptions.TOTAL: self.on_total,
            StatusOptions.PASSED: self.on_passed,
            StatusOptions.REMAINED: self.on_remained,
            StatusOptions.INTERVAL: self.on_interval
        }

        command = None
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in subhandlers:
            return subhandlers[command](args)

    def on_whatsup(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.all()

    def on_only(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.only()

    def on_today(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.today()

    def on_total(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.total()

    def on_passed(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.passed()

    def on_remained(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.remained()

    def on_interval(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.interval()


__all__ = ["StatusController"]
