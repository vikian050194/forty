import abc
from typing import List
from forty.actions import Action


class AbstractView(abc.ABC):
    pass


class StrView(AbstractView):
    def __init__(self, value: str):
        self.value = value


class ListView(AbstractView):
    def __init__(self, list: List[str]):
        self.list = list


class ActionView(AbstractView):
    def __init__(self, action: Action):
        self.action = action


__all__ = [
    "AbstractView",
    "StrView",
    "ListView",
    "ActionView"
]
