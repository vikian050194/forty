from typing import List

from forty.options import Options
from forty.views.base import AbstractView
from forty.actions import WorkOptions
from forty.common import hms_to_time, iso_to_date
from forty.views import ActionView, InfoView
from forty.models import WorkModel
from forty.decorators import check_after
from .abstract import AbstractController


class FinishController(AbstractController):
    def keys(self) -> List[str]:
        return [WorkOptions.FINISH]

    @check_after
    def handle(self, options: Options) -> AbstractView:
        model = WorkModel(self.fm, self.tm)
        new_time = None
        new_date = None
        if len(options.values) == 1:
            new_time = hms_to_time(options.values[0])
        if len(options.values) == 2:
            new_time = hms_to_time(options.values[1])
            new_date = iso_to_date(options.values[0])
        new_action = model.finish(new_date=new_date, new_time=new_time)
        if new_action:
            return ActionView(new_action.type, new_action.value, new_action.timestamp)
        else:
            return InfoView("already finished")


__all__ = ["FinishController"]
