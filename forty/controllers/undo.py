from typing import List

from forty.options import Options
from forty.views.base import AbstractView
from forty.actions import HistoryOptions
from forty.views import InfoView
from forty.models import HistoryModel
from forty.views.message import WarningView
from .abstract import AbstractController


class UndoController(AbstractController):
    def keys(self) -> List[str]:
        return [HistoryOptions.UNDO]

    def handle(self, options: Options) -> AbstractView:
        model = HistoryModel(self.pm, self.tm)
        expected_count = 1
        if options.values:
            expected_count = int(options.values[0])
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


__all__ = ["UndoController"]
