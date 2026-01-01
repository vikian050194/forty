from forty.actions import ProjectOptions
from forty.controllers.abstract import AbstractController
from forty.models.project import ProjectModel
from forty.views.base import StrView
from forty.views.message import InfoView


class ProjectGetController(AbstractController):
    def keys(self):
        return [ProjectOptions.GET]

    def handle(self, options):
        model = ProjectModel(self.fm, self.tm)
        current_project = model.get()
        if current_project:
            return StrView(current_project)
        else:
            return InfoView("current project is not specified")