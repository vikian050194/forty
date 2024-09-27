from forty.actions import Commands

from ..composite import CompositeController


class StatusController(CompositeController):
    def keys(self):
        return [Commands.STATUS]


__all__ = ["StatusController"]
