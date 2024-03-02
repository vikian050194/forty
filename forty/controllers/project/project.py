from forty.actions import Commands
from forty.views import *

from ..composite import CompositeController


class ProjectController(CompositeController):
    def keys(self):
        return [Commands.PROJECT]


__all__ = ["ProjectController"]
