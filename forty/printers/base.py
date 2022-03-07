import builtins


class BasePrinter():
    def __print__(self, message):
        builtins.print(message)

    def print_message(self, message):
        raise NotImplementedError()

    def print_info(self, message):
        raise NotImplementedError()

    def print_warning(self, message):
        raise NotImplementedError()

    def print_error(self, message):
        raise NotImplementedError()

    def print_list(self, list):
        raise NotImplementedError()

    def print_object(self, object):
        raise NotImplementedError()

    def print_log(self, list):
        raise NotImplementedError()


__all__ = ["BasePrinter"]
