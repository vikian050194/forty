import abc
import json

import builtins
from ..views import *
from ..configuration import Configuration, OutputFlagValues


class AbstractOutputManager(abc.ABC):
    @abc.abstractmethod
    def emmit(self,  message: AbstractView):
        raise NotImplementedError()


class BasePrinter():
    def __print__(self, message):
        builtins.print(message)

    def print_message(self, message):
        raise NotImplementedError()

    def print_list(self, list):
        raise NotImplementedError()

    def print_object(self, object):
        raise NotImplementedError()


class HumanPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(message)

    def print_list(self, list):
        for item in list:
            self.__print__(item)

    def print_object(self, object):
        for k, v in object.__dict__.items() :
            self.__print__(f"{k}: {v}")

class PlainPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(message)

    def print_list(self, list):
        self.__print__(" ".join(list))

    def print_object(self, object):
        for k, v in object.__dict__.items() :
            self.__print__(f"{k}: {v}")


class JsonPrinter(BasePrinter):
    def print_message(self, message):
        self.__print__(message)

    def print_list(self, list):
        self.__print__(json.dumps(list, sort_keys=True, indent=4))

    def print_object(self, object):
        self.__print__(json.dumps(object, sort_keys=True, indent=4))


class OutputManager():
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.printer = None

        if configuration.output == OutputFlagValues.HUMAN:
            self.printer = HumanPrinter()
        if configuration.output == OutputFlagValues.PLAIN:
            self.printer = PlainPrinter()
        if configuration.output == OutputFlagValues.JSON:
            self.printer = JsonPrinter()

    def __print_message__(self, message):
        self.printer.print_message(message)

    def __print_list__(self, list):
        self.printer.print_list(list)

    def __print_object__(self, object):
        self.printer.print_object(object)

    def emmit(self,  message: AbstractView):
        if type(message) is StrView:
            self.__print_message__(message.value)
        if type(message) is ListView:
            self.__print_list__(message.list)
        if type(message) is ActionView:
            self.__print_object__(message.action)


__all__ = ["OutputManager"]
