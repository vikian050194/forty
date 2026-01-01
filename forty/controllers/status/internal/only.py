from typing import List

from forty.actions import StatusOptions
from forty.controllers.abstract import AbstractController
from forty.decorators import check_before
from forty.models.status import StatusModel
from forty.options import Options
from forty.views.base import AbstractView


class StatusOnlyController(AbstractController):
    def keys(self) -> List[str]:
        return [StatusOptions.ONLY]

    @check_before
    def handle(self, options: Options) -> AbstractView:
        model = StatusModel(self.fm, self.tm)
        return model.only()


__all__ = ["StatusOnlyController"]
