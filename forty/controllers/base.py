from typing import List

from forty.controllers.abstract import AbstractController
from forty.managers.project_manager import ProjectManager
from forty.managers.time_manager import TimeManager


class BaseController(AbstractController):
    def __init__(self, pm: ProjectManager, tm: TimeManager, cs: List[AbstractController]):
        super().__init__(pm, tm)
        self.handlers = {}
        for c in cs:
            for key in c.keys():
                self.handlers[key] = c

    def keys(self):
        return self.handlers.keys()


__all__ = ["BaseController"]
