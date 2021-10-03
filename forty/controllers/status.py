from typing import List

from .base import AbstractController
from ..actions import StatusOptions
from ..reducers import *
from ..views import StrView, ListView
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
        self.handlers[StatusOptions.TILL] = self.handle_till


    def handle_whatsup(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        all_values = model.all()
        return ListView(all_values)

    def handle_status(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        [status_value] = model.status()
        return StrView(status_value)

    def handle_today(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        today_values = model.today()
        return ListView(today_values)

    def handle_total(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        total_values = model.total()
        return ListView(total_values)

    def handle_passed(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        passed_values = model.passed()
        return ListView(passed_values)

    def handle_remained(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        remained_values = model.remained()
        return ListView(remained_values)

    def handle_till(self, options: List[str]):
        model = StatusModel(self.pm, self.tm)
        till_values = model.till()
        return ListView(till_values)


__all__ = ["StatusController"]
