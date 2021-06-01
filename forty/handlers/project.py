from typing import List

from .base import BaseHandler
from ..actions import Commands, ProjectOptions


def on_get(pm, options):
    current_project = pm.load_project()
    print(current_project)


def on_list(pm, options):
    projects_list = pm.get_projects_list()
    for project in projects_list:
        print(project)


def on_new(pm, options):
    [name] = options
    pm.initialize_new_project(name)


def on_set(pm, options):
    [name] = options
    pm.select_project(name)
    pm.save_project()


handlers = {
    ProjectOptions.LIST: on_list,
    ProjectOptions.NEW: on_new,
    ProjectOptions.GET: on_get,
    ProjectOptions.SET: on_set
}


class ProjectHandler(BaseHandler):
    @property
    def key(self):
        return Commands.PROJECT

    def handle(self, options: List[str]):
        command = None
        args = []

        if len(options) > 0:
            command = options[0]

        if len(options) > 1:
            args = options[1:]

        if command in handlers:
            return handlers[command](self.pm, args)
        else:
            return False


__all__ = ["ProjectHandler"]
