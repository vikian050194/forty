from typing import List

from .base import BasePrinter
from ..actions import Action, Actions


class HumanPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(message)

    def print_list(self, list):
        for item in list:
            self.__print__(item)

    def print_object(self, object):
        for k, v in object.__dict__.items():
            self.__print__(f"{k}: {v}")

    def print_log(self, list: List[Action]):
        max_len = max([len(action_type.value) for action_type in Actions])
        for item in list:
            line = f"{item.type.ljust(max_len)} {item.timestamp}"
            self.__print__(line)


__all__ = ["HumanPrinter"]
