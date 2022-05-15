import enum


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
