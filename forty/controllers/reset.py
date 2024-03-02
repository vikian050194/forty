from typing import List

from forty.options import Options
from forty.views.base import AbstractView
from forty.actions import HistoryOptions
from forty.models import HistoryModel
from forty.views.message import InfoView
from .abstract import AbstractController


class ResetController(AbstractController):
    def keys(self) -> List[str]:
        return [HistoryOptions.RESET]

    def handle(self, options: Options) -> AbstractView:
        model = HistoryModel(self.pm, self.tm)
        model.reset()
        return InfoView("all actions are deleted")


__all__ = ["ResetController"]
