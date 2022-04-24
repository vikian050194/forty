from typing import List

from .base import AbstractView


class ActionLogView(AbstractView):
    def __init__(self, type, value, timestamp):
        self.type = type
        self.value = value
        self.timestamp = timestamp


class LogView(AbstractView):
    def __init__(self, list: List[ActionLogView]):
        self.list = list


__all__ = [
    "ActionLogView",
    "LogView"
]
