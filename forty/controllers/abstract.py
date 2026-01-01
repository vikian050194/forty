import abc
from typing import List

from forty.managers import FileManager, TimeManager
from forty.options import Options
from forty.views.base import AbstractView


class AbstractController(abc.ABC):
    def __init__(self, fm: FileManager, tm: TimeManager):
        self.fm = fm
        self.tm = tm

    @abc.abstractmethod
    def keys(self) -> List[str]:
        pass

    @abc.abstractmethod
    def handle(self, options: Options) -> AbstractView:
        pass


__all__ = ["AbstractController"]
