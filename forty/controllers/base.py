import abc
from typing import List

from ..actions import ActionType
from ..managers import ProjectManager, TimeManager


class AbstractController(abc.ABC):
    def __init__(self, pm: ProjectManager, tm: TimeManager):
        self.pm = pm
        self.tm = tm

    @property
    @abc.abstractmethod
    def key(self) -> ActionType:
        raise NotImplementedError()

    @abc.abstractmethod
    def handle(self, options: List[str]):
        raise NotImplementedError()


__all__ = ["AbstractController"]
