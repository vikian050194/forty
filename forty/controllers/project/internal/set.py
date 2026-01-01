from forty.actions import ProjectOptions
from forty.controllers.abstract import AbstractController
from forty.models.project import ProjectModel
from forty.options import Options
from forty.views.base import AbstractView, ListView
from forty.views.message import ErrorView, InfoView


class ProjectSetController(AbstractController):
    def keys(self):
        return [ProjectOptions.SET]

    def _complete(self, value: str) -> AbstractView:
        suggestions = []

        model = ProjectModel(self.fm, self.tm)
        possible_values = model.list()

        if value:
            for possible_value in possible_values:
                if str(possible_value).startswith(value):
                    suggestions.append(possible_value)
        if suggestions:
            return ListView(suggestions)

        for possible_value in possible_values:
            suggestions.append(possible_value)
        # TODO should we return error on wrong value that does not match any possible value?
        return ListView(suggestions)

    def _handle(self, value: str) -> AbstractView:
        model = ProjectModel(self.fm, self.tm)
        if not value:
            return ErrorView("project name is not specified")
        set_project_name = model.set(value)
        if set_project_name:
            return InfoView(set_project_name)
        return ErrorView(f"project \"{value}\" is not found")

    def handle(self, options: Options):
        value = None

        if len(options.values) > 0:
            value = options.values[0]

        # TODO implement unexpected arguments passing handling
        # if len(options.values) > 1:
        #     return ErrorView("project name is not specified")

        if options.complete:
            return self._complete(value=value)

        return self._handle(value=value)
