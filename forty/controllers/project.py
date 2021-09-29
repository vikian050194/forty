from typing import List

from .base import AbstractController
from ..actions import Commands, ProjectOptions
from ..models import ProjectModel
from ..views import *


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
        # TODO what if there is no project?
        return StrView(current_project)

    def on_list(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        projects_list = model.list()
        return ListView(projects_list)
        
    def on_new(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        [name] = options
        new_project_name = model.new(name)
        return StrView(new_project_name)

    def on_set(self, options: List[str]):
        model = ProjectModel(self.pm, self.tm)
        [name] = options
        set_project_name = model.set(name)
        if set_project_name:
            return StrView(set_project_name)
        else:
            return StrView(f"project {name} is not found")


__all__ = ["ProjectController"]
