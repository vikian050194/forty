from forty.actions import ProjectOptions
from forty.controllers.abstract import AbstractController
from forty.models.project import ProjectModel
from forty.views.message import ErrorView, InfoView


class ProjectNewController(AbstractController):
    def keys(self):
        return [ProjectOptions.NEW]

    def handle(self, options):
        model = ProjectModel(self.fm, self.tm)
        if not options.values:
            return ErrorView("new project name is not specified")
        [name] = options.values
        new_project_name = model.new(name)
        if new_project_name:
            return InfoView(new_project_name)
        else:
            return ErrorView(f'project "{name}" could not be created')