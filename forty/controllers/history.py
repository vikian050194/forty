from typing import List

from .base import AbstractController
from ..actions import Commands, HistoryOptions
from ..views import LogView, InfoView, WarningView, ListView, StrView
from ..models import HistoryModel
from ..common import iso_to_date


class HistoryController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.HISTORY] = self.handle_subcommand
        self.handlers[Commands.LOG] = self.handle_log

    def handle_subcommand(self, options: List[str]):
        subhandlers = {
            HistoryOptions.RESET: self.on_reset,
            HistoryOptions.UNDO: self.on_undo,
            HistoryOptions.DATE: self.on_date,
            HistoryOptions.CHECK: self.on_check,
        }

        command = None
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in subhandlers:
            return subhandlers[command](args)

    def handle_log(self, options: List[str]):
        model = HistoryModel(self.pm, self.tm)
        actions = model.log()
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
