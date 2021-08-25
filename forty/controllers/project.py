from typing import List

from .base import AbstractController
from ..actions import Commands, ProjectOptions
from ..models import ProjectModel
from ..views import *


class ProjectController(AbstractController):
    @property
    def key(self):
        return Commands.PROJECT

    def handle(self, options: List[str]):
        controllers = {
            ProjectOptions.LIST: self.on_list,
            ProjectOptions.NEW: self.on_new,
            ProjectOptions.GET: self.on_get,
            ProjectOptions.SET: self.on_set
        }

        command = None
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in controllers:
            return controllers[command](args)

    def on_get(self, options):
        model = ProjectModel(self.pm, self.tm)
        current_project = model.get()
        # TODO what if there is no project?
        return StrView(current_project)

    def on_list(self, options):
        model = ProjectModel(self.pm, self.tm)
        projects_list = model.list()
        return ListView(projects_list)
        
    def on_new(self, options):
        model = ProjectModel(self.pm, self.tm)
        [name] = options
        new_project_name = model.new(name)
        return StrView(new_project_name)

    def on_set(self, options):
        model = ProjectModel(self.pm, self.tm)
        [name] = options
        set_project_name = model.set(name)
        if set_project_name:
            return StrView(set_project_name)
        else:
            return StrView("not found")


__all__ = ["ProjectController"]
