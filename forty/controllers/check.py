from typing import List
from forty.common import iso_to_date

from forty.options import Options
from forty.views.base import AbstractView, ListView, StrView
from forty.actions import HistoryOptions
from forty.models import HistoryModel
from forty.views.message import InfoView
from .abstract import AbstractController


class CheckController(AbstractController):
    def keys(self) -> List[str]:
        return [HistoryOptions.CHECK]

    def handle(self, options: Options) -> AbstractView:
        model = HistoryModel(self.pm, self.tm)
        if options.values:
            day = iso_to_date(options.values[0])
            is_ok = model.check(day)
            result_str = "OK" if is_ok else "bad"
            return StrView(f"{options.values[0]} is {result_str}")
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


__all__ = ["CheckController"]
