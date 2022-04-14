import abc
from typing import List

from ..managers import ProjectManager, TimeManager


class AbstractController(abc.ABC):
    def __init__(self, pm: ProjectManager, tm: TimeManager):
        self.pm = pm
        self.tm = tm
        self.handlers = {}

    @property
    def keys(self):
        return self.handlers.keys()

    def handle(self, options: List[str]):
        command = None
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in self.handlers:
            return self.handlers[command](args)
        return None


__all__ = ["AbstractController"]
