from forty.actions import Commands

from ..composite import CompositeController

from .internal import *


class StatusController(CompositeController):
    def __init__(self, pm, tm):
        cs = [
            StatusFullController(pm, tm),
            StatusIntervalController(pm, tm),
            StatusOnlyController(pm, tm),
            StatusPassedController(pm, tm),
            StatusRemainedController(pm, tm),
            StatusTodayController(pm, tm),
            StatusTotalController(pm, tm)
        ]
        super().__init__(pm, tm, cs)

    def keys(self):
        return [Commands.STATUS]


__all__ = ["StatusController"]
