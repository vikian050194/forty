from typing import List

from .base import AbstractController
from ..actions import StatusOptions
from ..reducers import *
from ..models import StatusModel


class StatusController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[StatusOptions.WHATSUP] = self.handle_whatsup
        self.handlers[StatusOptions.STATUS] = self.handle_status
        self.handlers[StatusOptions.TODAY] = self.handle_today
        self.handlers[StatusOptions.TOTAL] = self.handle_total
        self.handlers[StatusOptions.PASSED] = self.handle_passed
        self.handlers[StatusOptions.REMAINED] = self.handle_remained
        self.handlers[StatusOptions.INTERVAL] = self.handle_interval


    def handle_whatsup(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.all()

    def handle_status(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.status()

    def handle_today(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.today()

    def handle_total(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.total()

    def handle_passed(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.passed()

    def handle_remained(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.remained()

    def handle_interval(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        return model.interval()


__all__ = ["StatusController"]
