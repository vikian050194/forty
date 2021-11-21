from typing import List

from datetime import time, timedelta

from .base import BasePrinter
from ..common import time_to_hms, timedelta_to_hms
from ..actions import Action, Actions


def to_str(value):
    if type(value) is time:
        return time_to_hms(value)
    if type(value) is timedelta:
        return timedelta_to_hms(value)
    return value


class HumanPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(to_str(message))

    def print_list(self, list):
        for item in list:
            self.__print__(item)

    def print_object(self, object):
        for k, v in object.__dict__.items():
            self.__print__(f"{k}: {to_str(v)}")

    def print_log(self, list: List[Action]):
        max_len = max([len(action_type.value) for action_type in Actions])
        for item in list:
            line = f"{item.type.ljust(max_len)} {item.timestamp}"
            self.__print__(line)


__all__ = ["HumanPrinter"]
