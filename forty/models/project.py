from .base import AbstractModel


class ProjectModel(AbstractModel):
    def get(self):
        current_project = self.pm.load_project()
        return current_project

    def list(self):
        projects_list = self.pm.get_projects_list()
        sorted_projects_list = list(sorted(projects_list))
        return sorted_projects_list

    def new(self, name):
        self.pm.initialize_new_project(name)
        return name

    def set(self, name):
        projects_list = self.pm.get_projects_list()
        if name in projects_list:
            self.pm.select_project(name)
            self.pm.save_project()
            return name
        return None


__all__ = ["ProjectModel"]
