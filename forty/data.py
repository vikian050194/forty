import json
from datetime import datetime
from pathlib import Path

from .actions import Action
from .common import to_iso


home = str(Path.home())
dir = home + "/.forty"
file_config = dir + "/config.json"
file_actions = dir + "/actions.json"


class Config():
    def __init__(self, total: int, day: int):
        self.total = total
        self.day = day

    def to_dict(self):
        return {
            "total": self.total,
            "day": self.day
        }


def load_config() -> Config:
    with open(file_config, "r") as fr:
        values = json.load(fr)
        return Config(values["total"], values["day"])


def save_config(config: Config):
    with open(file_config, "w") as fw:
        json.dump(config.to_dict(), fw)


def make_action(data):
    type = data.get("type")
    value = data.get("value")
    timestamp = datetime.fromisoformat(data.get("timestamp"))
    return Action(type, timestamp, value)


def load_actions():
    with open(file_actions, "r") as fr:
        return list(map(make_action, json.load(fr)))


def save_actions(actions):
    data = list(map(lambda item: item.to_dict(), actions))
    with open(file_actions, "w") as fw:
        json.dump(data, fw)