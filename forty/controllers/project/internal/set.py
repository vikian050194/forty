from forty.actions import ProjectOptions
from forty.controllers.abstract import AbstractController
from forty.models.project import ProjectModel
from forty.views.message import ErrorView, InfoView


class ProjectSetController(AbstractController):
    def keys(self):
        return [ProjectOptions.SET]

    def handle(self, options):
        model = ProjectModel(self.pm, self.tm)
        if not options.values:
            return ErrorView("project name is not specified")
        [name] = options.values
        set_project_name = model.set(name)
        if set_project_name:
            return InfoView(set_project_name)
        else:
            return ErrorView(f"project \"{name}\" is not found")