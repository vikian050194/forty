from typing import List

from .base import AbstractView
from ..actions import Action


class LogView(AbstractView):
    def __init__(self, list: List[Action]):
        self.list = list


__all__ = ["LogView"]
