from typing import List

from forty.options import Options
from forty.views.base import AbstractView, ListView
from forty.actions import HistoryOptions
from forty.models import HistoryModel
from forty.views.message import InfoView
from .abstract import AbstractController


class DateController(AbstractController):
    def keys(self) -> List[str]:
        return [HistoryOptions.DATE]

    def handle(self, options: Options) -> AbstractView:
        model = HistoryModel(self.fm, self.tm)
        dates = model.date()
        if dates:
            return ListView(dates)
        else:
            return InfoView("there are no dates")


__all__ = ["DateController"]
