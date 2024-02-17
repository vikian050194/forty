from typing import List

from .base import AbstractController
from forty.actions import Commands, ProjectOptions
from forty.models import ProjectModel
from forty.views import *


class ProjectController(AbstractController):
    def __init__(self, pm, tm):
        super().__init__(pm, tm)
        self.handlers[Commands.PROJECT] = self.handle_subcommand

    def handle_subcommand(self, options: List[str]):
        subhandlers = {
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

        if command in subhandlers:
            return subhandlers[command](args)

    def on_get(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        current_project = model.get()
        if current_project:
            return StrView(current_project)
        else:
            return InfoView("current project is not specified")

    def on_list(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        projects_list = model.list()
        if projects_list:
            return ListView(projects_list)
        else:
            return InfoView("there are no projects")
        
    def on_new(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        if not options:
            return ErrorView("new project name is not specified")
        [name] = options
        new_project_name = model.new(name)
        if new_project_name:
            return InfoView(new_project_name)
        else:
            return ErrorView(f"project \"{name}\" could not be created")

    def on_set(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        if not options:
            return ErrorView("project name is not specified")
        [name] = options
        set_project_name = model.set(name)
        if set_project_name:
            return InfoView(set_project_name)
        else:
            return ErrorView(f"project \"{name}\" is not found")


__all__ = ["ProjectController"]
