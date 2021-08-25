import enum


@enum.unique
class OutputFlagValues(str, enum.Enum):
    HUMAN = "human"
    PLAIN = "plain"
    JSON = "json"


class Flag():
    def __init__(self, short_name: str, full_name: str, values: enum.Enum):
        self.__values__ = values
        self.__short_name__ = short_name
        self.__full_name__ = full_name

    @property
    def short_name(self):
        return self.__short_name__

    @property
    def full_name(self):
        return self.__full_name__


class Configuration():
    def __init__(self, home: str, output: str):
        self._home = home
        self._output = output if output else OutputFlagValues.HUMAN

    @property
    def home(self):
        return self._home

    @property
    def output(self):
        return self._output
