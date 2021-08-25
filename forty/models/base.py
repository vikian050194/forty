import abc

from ..managers import ProjectManager, TimeManager


class AbstractModel(abc.ABC):
    def __init__(self, pm: ProjectManager, tm: TimeManager):
        self.pm = pm
        self.tm = tm


__all__ = ["AbstractModel"]
