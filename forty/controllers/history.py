from typing import List

from .base import AbstractController
from forty.actions import HistoryOptions
from forty.views import ActionLogView, LogView, InfoView, WarningView, ListView, StrView
from forty.models import HistoryModel
from forty.common import iso_to_date


class HistoryController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[HistoryOptions.LOG] = self.on_log
        self.handlers[HistoryOptions.RESET] = self.on_reset
        self.handlers[HistoryOptions.UNDO] = self.on_undo
        self.handlers[HistoryOptions.DATE] = self.on_date
        self.handlers[HistoryOptions.CHECK] = self.on_check

    def on_log(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        actions = model.log()
        actions = list(map(lambda a: ActionLogView(a.type, a.value, a.timestamp), actions))
        return LogView(actions)

    def on_reset(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        model.reset()
        return InfoView("all actions are deleted")

    def on_date(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        dates = model.date()
        if dates:
            return ListView(dates)
        else:
            return InfoView("there are no dates")

    def on_undo(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        expected_count = 1
        if options:
            expected_count = int(options[0])
        actual_count = model.undo(expected_count)
        if actual_count == 1:
            message = "last 1 action is deleted"
        elif actual_count == 0:
            message = "no actions are deleted"
        else:
            message = f"last {actual_count} actions are deleted"
        if expected_count != actual_count:
            return WarningView(message)
        else:
            return InfoView(message)

    def on_check(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        if options:
            day = iso_to_date(options[0])
            is_ok = model.check(day)
            result_str = "OK" if is_ok else "bad"
            return StrView(f"{options[0]} is {result_str}")
        else:
            results = []
            dates = model.date()
            for date in dates:
                is_ok = model.check(date)
                result_str = "OK" if is_ok else "bad"
                check_result = f"{date} is {result_str}"
                results.append(check_result)
            if results:
                return ListView(results)
            else:
                return InfoView("there is nothing to check")


__all__ = ["HistoryController"]
