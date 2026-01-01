from .base import AbstractModel


class ProjectModel(AbstractModel):
    def get(self):
        current_project = self.fm.load_project()
        return current_project

    def list(self):
        projects_list = self.fm.get_projects_list()
        sorted_projects_list = list(sorted(projects_list))
        return sorted_projects_list

    def new(self, name):
        projects_list = self.fm.get_projects_list()
        if not name in projects_list:
            self.fm.initialize_new_project(name)
            return name
        return None

    def set(self, name):
        projects_list = self.fm.get_projects_list()
        if name in projects_list:
            self.fm.select_project(name)
            self.fm.save_project()
            return name
        return None


__all__ = ["ProjectModel"]
