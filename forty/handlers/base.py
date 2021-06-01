import abc
from typing import List, Union

from ..actions import Commands, Actions
from ..project_manager import ProjectManager


class BaseHandler(abc.ABC):
    def __init__(self, pm: ProjectManager):
        self.pm = pm

    @property
    @abc.abstractmethod
    def key(self) -> Union[Actions, Commands]:
        raise NotImplementedError()

    @abc.abstractmethod
    def handle(self, options: List[str]):
        raise NotImplementedError()


__all__ = ["BaseHandler"]
