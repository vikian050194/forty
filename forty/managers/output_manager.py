import abc

from forty.views import *
from forty.printers import *
from forty.configuration import Configuration, OutputFlagValues


class AbstractOutputManager(abc.ABC):
    @abc.abstractmethod
    def emmit(self,  view: AbstractView):
        raise NotImplementedError()


class OutputManager(AbstractOutputManager):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.printer: BasePrinter = None

        if configuration.output == OutputFlagValues.HUMAN:
            self.printer = HumanPrinter()
        if configuration.output == OutputFlagValues.PLAIN:
            self.printer = PlainPrinter()
        if configuration.output == OutputFlagValues.JSON:
            self.printer = JsonPrinter()

    def __print_str__(self, message):
        self.printer.print_str(message)

    def __print_message__(self, message: MessageView):
        self.printer.print_message(message)

    def __print_list__(self, list):
        self.printer.print_list(list)

    def __print_object__(self, object):
        self.printer.print_object(object)

    def __print_log__(self, log):
        self.printer.print_log(log)


    def emmit(self,  view: AbstractView):
        if type(view) is StrView:
            self.__print_str__(view)
        elif type(view) is InfoView:
            self.__print_message__(view)
        elif type(view) is WarningView:
            self.__print_message__(view)
        elif type(view) is ErrorView:
            self.__print_message__(view)
        elif type(view) is ListView:
            self.__print_list__(view.list)
        elif type(view) is ActionView:
            self.__print_object__(view)
        elif type(view) is LogView:
            self.__print_log__(view.list)
        elif type(view) is FullStatusView:
            self.__print_object__(view)
        elif type(view) is TodayStatusView:
            self.__print_object__(view)
        elif type(view) is TotalStatusView:
            self.__print_object__(view)
        elif type(view) is PassedStatusView:
            self.__print_object__(view)
        elif type(view) is RemainedStatusView:
            self.__print_object__(view)
        elif type(view) is IntervalStatusView:
            self.__print_object__(view)
        elif type(view) is OnlyStatusView:
            self.__print_object__(view)
        else:
            self.__print_str__("unknown view")


__all__ = ["OutputManager"]
