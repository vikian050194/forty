from forty.actions import Commands

from ..composite import CompositeController

from .internal import *


class ProjectController(CompositeController):
    def __init__(self, pm, tm):
        cs = [
            ProjectListController(pm, tm),
            ProjectNewController(pm, tm),
            ProjectGetController(pm, tm),
            ProjectSetController(pm, tm)
        ]
        super().__init__(pm, tm, cs)

    def keys(self):
        return [Commands.PROJECT]


__all__ = ["ProjectController"]
