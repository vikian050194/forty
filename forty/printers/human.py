from typing import List

from forty.views.log import ActionLogView

from .base import BasePrinter, to_str
from forty.actions import WorkOptions


class HumanPrinter(BasePrinter):
    def print_str(self, message):
        self.__print__(to_str(message.value))

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

    def print_message(self, message):
        self.__print__(f"{message.level}: {to_str(message.value)}")

    def print_list(self, list):
        for item in list:
            self.__print__(item)
    
    def print_log(self, list: List[ActionLogView]):
        max_len = max([len(action_type.value) for action_type in WorkOptions])
        for item in list:
            line = f"{item.type.ljust(max_len)} {item.timestamp}"
            self.__print__(line)


__all__ = ["HumanPrinter"]
