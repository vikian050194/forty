from forty.actions import Commands

from ..composite import CompositeController


class ProjectController(CompositeController):
    def keys(self):
        return [Commands.PROJECT]


__all__ = ["ProjectController"]
