from typing import List

from .base import AbstractController
from ..actions import Commands, HistoryOptions
from ..views import LogView, InfoView, WarningView
from ..models import HistoryModel


class HistoryController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.HISTORY] = self.handle_subcommand
        self.handlers[Commands.LOG] = self.handle_log

    def handle_subcommand(self, options: List[str]):
        subhandlers = {
            HistoryOptions.RESET: self.on_reset,
            HistoryOptions.UNDO: self.on_undo
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


__all__ = ["HistoryController"]
