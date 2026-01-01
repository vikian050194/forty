from typing import List

from forty.options import Options
from forty.views.base import AbstractView
from forty.actions import HistoryOptions
from forty.models import HistoryModel
from forty.views.log import ActionLogView, LogView
from .abstract import AbstractController


class LogController(AbstractController):
    def keys(self) -> List[str]:
        return [HistoryOptions.LOG]

    def handle(self, options: Options) -> AbstractView:
        model = HistoryModel(self.fm, self.tm)
        actions = model.log()
        actions = list(map(lambda a: ActionLogView(a.type, a.value, a.timestamp), actions))
        return LogView(actions)


__all__ = ["LogController"]
