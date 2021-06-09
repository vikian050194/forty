import abc
from typing import List, Union

from ..actions import Commands, Actions
from ..managers import ProjectManager, OutputManager, TimeManager


class AbstractHandler(abc.ABC):
    def __init__(self, pm: ProjectManager, om: OutputManager, tm: TimeManager):
        self.pm = pm
        self.om = om
        self.tm = tm

    @property
    @abc.abstractmethod
    def key(self) -> Union[Actions, Commands]:
        raise NotImplementedError()

    @abc.abstractmethod
    def handle(self, options: List[str]):
        raise NotImplementedError()


__all__ = ["AbstractHandler"]
