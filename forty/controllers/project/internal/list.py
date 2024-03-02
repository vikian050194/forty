from forty.actions import ProjectOptions
from forty.controllers.abstract import AbstractController
from forty.models.project import ProjectModel
from forty.views.base import ListView
from forty.views.message import InfoView


class ProjectListController(AbstractController):
    def keys(self):
        return [ProjectOptions.LIST]
    
    def handle(self, options):
        model = ProjectModel(self.pm, self.tm)
        projects_list = model.list()
        if projects_list:
            return ListView(projects_list)
        else:
            return InfoView("there are no projects")