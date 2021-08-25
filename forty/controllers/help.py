from typing import List

from .base import AbstractController
from ..actions import Commands, Actions, ActionType


def print_option(option: ActionType, hint):
    print(f"{option.value}\t{hint}")


class HelpController(AbstractController):
    @property
    def key(self):
        return Commands.HELP

    def handle(self, options: List[str]):
        print("forty", "v0.1.0")
        # TODO use OutputManager
        print_option(Commands.HELP, "get help")
        print_option(Commands.PROJECT, "TBD")
        print_option(Commands.GET, "TBD")
        # print_option(Commands.STATUS, "get status")
        # print_option(Commands.RESET, "reset actions")
        # print_option(Commands.PLUS, "plus delta time")
        # print_option(Commands.MINUS, "minus delta time")
        # print_option(Commands.BREAK, "start pause and automatically finish it after hh:mm:ss")
        # print_option(Commands.CONFIG, "get or set configuration parameters")

        print_option(Actions.START, "start work")
        print_option(Actions.FINISH, "finish work")
        # print_option(Actions.PAUSE, "pause work")
        # print_option(Actions.RESUME, "resume work")


__all__ = ["HelpController"]
