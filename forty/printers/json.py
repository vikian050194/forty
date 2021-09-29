import json

from .base import BasePrinter


class JsonPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(message)

    def print_list(self, list):
        self.__print__(json.dumps(list, sort_keys=True, indent=4))

    def print_object(self, object):
        self.__print__(json.dumps(object, sort_keys=True, indent=4))

    def print_log(self, list):
        objects = [item.to_dict() for item in list]
        self.print_list(objects)


__all__ = ["JsonPrinter"]
