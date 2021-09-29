from .base import BasePrinter


class PlainPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(message)

    def print_list(self, list):
        self.__print__(" ".join(list))

    def print_object(self, object):
        for k, v in object.__dict__.items() :
            self.__print__(f"{k}: {v}")

    def print_log(self, list):
        for item in list:
            line = f"{item.type} {item.timestamp}"
            self.__print__(line)


__all__ = ["PlainPrinter"]
