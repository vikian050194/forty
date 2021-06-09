from typing import List

from .base import AbstractHandler
from ..actions import Commands, ProjectOptions


def on_get(pm, om, options):
    project = pm.load_project()
    om.emmit(message=project)


def on_list(pm, om, options):
    projects_list = pm.get_projects_list()
    for project in sorted(projects_list):
        om.emmit(project, use_notify=False)


def on_new(pm, om, options):
    [name] = options
    pm.initialize_new_project(name)
    om.emmit(name)


def on_set(pm, om, options):
    [name] = options
    projects_list = pm.get_projects_list()
    if name in projects_list:
        pm.select_project(name)
        pm.save_project()
        om.emmit(name)
        return
    on_list(pm, om, [])


handlers = {
    ProjectOptions.LIST: on_list,
    ProjectOptions.NEW: on_new,
    ProjectOptions.GET: on_get,
    ProjectOptions.SET: on_set
}


class ProjectHandler(AbstractHandler):
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
            handlers[command](self.pm, self.om, args)


__all__ = ["ProjectHandler"]
