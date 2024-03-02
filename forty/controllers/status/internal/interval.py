from typing import List

from forty.actions import StatusOptions
from forty.controllers.abstract import AbstractController
from forty.decorators import check_before
from forty.models.status import StatusModel
from forty.options import Options
from forty.views.base import AbstractView


class StatusIntervalController(AbstractController):
    def keys(self) -> List[str]:
        return [StatusOptions.INTERVAL]

    @check_before
    def handle(self, options: Options) -> AbstractView:
        model = StatusModel(self.pm, self.tm)
        return model.interval()


__all__ = ["StatusIntervalController"]
