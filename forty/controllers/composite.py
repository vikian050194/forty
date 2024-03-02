from typing import List

from forty.controllers.abstract import AbstractController
from forty.managers.project_manager import ProjectManager
from forty.managers.time_manager import TimeManager
from forty.options import Options
from forty.views.base import ListView
from forty.views.message import ErrorView


class CompositeController(AbstractController):
    def __init__(self, pm: ProjectManager, tm: TimeManager, cs: List[AbstractController]):
        super().__init__(pm, tm)
        self.handlers = {}
        for c in cs:
            for key in c.keys():
                self.handlers[key] = c

    def keys(self):
        return self.handlers.keys()

    def handle(self, options: Options):
        command = None
        args = []

        if len(options.values) > 0:
            command = options.values[0]

        if len(options.values) > 1:
            args = options.values[1:]

        if options.complete:
            suggestions = []

            if command:
                for key in self.handlers.keys():
                    # TODO fix enum and string mixed usage
                    if key.value == command:
                        # TODO extract options instance
                        return self.handlers[command].handle(Options(args, True))

                    # TODO fix enum and string mixed usage
                    if str(key.value).startswith(command):
                        suggestions.append(key.value)

            if not suggestions:
                for key in self.handlers.keys():
                    # TODO fix enum and string mixed usage
                    suggestions.append(key.value)

            return ListView(suggestions)

        if command in self.handlers:
            # TODO extract options instance
            return self.handlers[command].handle(Options(args, False))
        
        if command:
            return ErrorView(f'command "{command}" is not found, please try "help"')
        
        return ErrorView(f'command is missed, please try "help"')


__all__ = ["CompositeController"]
