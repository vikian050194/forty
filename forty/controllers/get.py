from typing import List

from .base import AbstractController
from ..actions import Commands, GetOptions
from ..reducers import *
from ..views import StrView, ListView
from ..models import GetModel


class GetController(AbstractController):
    @property
    def key(self):
        return Commands.GET

    def handle(self, options: List[str]):
        controllers = {
            GetOptions.ALL: self.on_all,
            GetOptions.STATUS: self.on_status,
            GetOptions.TODAY: self.on_today,
            GetOptions.TOTAL: self.on_total,
            GetOptions.PASSED: self.on_passed,
            GetOptions.REMAINED: self.on_remained
        }

        command = GetOptions.ALL
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in controllers:
            return controllers[command]()

    def on_all(self):
        model = GetModel(self.pm, self.tm)
        all_values = model.all()
        return ListView(all_values)

    def on_status(self):
        model = GetModel(self.pm, self.tm)
        [status_value] = model.status()
        return StrView(status_value)

    def on_today(self):
        model = GetModel(self.pm, self.tm)
        today_values = model.today()
        return ListView(today_values)

    def on_total(self):
        model = GetModel(self.pm, self.tm)
        total_values = model.total()
        return ListView(total_values)

    def on_passed(self):
        model = GetModel(self.pm, self.tm)
        passed_values = model.passed()
        return ListView(passed_values)

    def on_remained(self):
        model = GetModel(self.pm, self.tm)
        remained_values = model.remained()
        return ListView(remained_values)


__all__ = ["GetController"]
