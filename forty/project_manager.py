import os
import json
from datetime import datetime
from pathlib import Path

from .actions import Action
from .common import to_ymd


def to_action(data):
    type = data.get("type")
    value = data.get("value")
    timestamp = datetime.fromisoformat(data.get("timestamp"))
    return Action(type, timestamp, value)


class Config():
    def __init__(self, day_limit: int = None, total_limit: int = None):
        self.day_limit = day_limit
        self.total_limit = total_limit
        self.type = type
    
    def to_dict(self):
        return dict(
            day_limit=self.day_limit,
            total_limit=self.total_limit
        )


class ProjectManager():
    def __init__(self, home: str = None):
        self.home = home
        self.dir = f"{self.home}/.forty"
        self.project = ""
        self.file_project = f"{self.dir}/PROJECT"

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        if not os.path.exists(self.file_project):
            self.save_project()

    def __get_project_dir(self):
        return f"{self.dir}/{self.project}"

    def __get_config_file(self):
        return f"{self.__get_project_dir()}/config.json"

    def __get_actions_file(self):
        return f"{self.__get_project_dir()}/actions.json"

    def get_projects_list(self):
        return [f for f in os.listdir(self.dir) if os.path.isdir(os.path.join(self.dir, f))]

    def is_project_selected(self):
        return self.project != ""

    def select_project(self, project_name: str):
        self.project = project_name

    def load_project(self):
        with open(self.file_project, "r") as fr:
            self.project = fr.readline()
            return self.project

    def save_project(self):
        with open(self.file_project, "w") as fw:
            fw.write(self.project)
            return self.project

    def load_config(self) -> Config:
        if not self.is_project_selected():
            raise Exception()

        with open(self.__get_config_file(), "r") as fr:
            values = json.load(fr)
            config = Config(values["day_limit"], values["total_limit"])
            config.today = to_ymd(datetime.now())
            return config

    def save_config(self, config: Config):
        if not self.is_project_selected():
            raise Exception()
        
        with open(self.__get_config_file(), "w") as fw:
            json.dump(config.to_dict(), fw)

    def load_actions(self):
        if not self.is_project_selected():
            raise Exception()

        with open(self.__get_actions_file(), "r") as fr:
            return list(map(to_action, json.load(fr)))

    def save_actions(self, actions):
        if not self.is_project_selected():
            raise Exception()

        data = list(map(lambda item: item.to_dict(), actions))
        with open(self.__get_actions_file(), "w") as fw:
            json.dump(data, fw)

    def initialize_new_project(self, project_name: str):
        self.select_project(project_name)

        project_dir = self.__get_project_dir()
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        self.save_project()

        default_actions = []
        self.save_actions(default_actions)
        
        default_config = Config(day_limit = None, total_limit = None)
        self.save_config(default_config)
