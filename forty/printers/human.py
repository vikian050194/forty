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
        object_dict = object.__dict__
        keys = list(object_dict.keys())
        max_len = max([len(key) for key in keys])
        for key in keys:
            delta_space = max_len - len(key)
            if delta_space != 1:
                delta_space = delta_space + 1
            line = f"{key}:{' '.ljust(delta_space)}{to_str(object_dict[key])}"
            self.__print__(line)

    def print_log(self, list: List[Action]):
        max_len = max([len(action_type.value) for action_type in Actions])
        for item in list:
            line = f"{item.type.ljust(max_len)} {item.timestamp}"
            self.__print__(line)


__all__ = ["HumanPrinter"]
