from typing import List

from .actions import Commands
from .controllers import controllers
from .managers import ProjectManager, OutputManager, TimeManager
from .configuration import Configuration


def main(options: List[str], configuration: Configuration):
    pm = ProjectManager(configuration)
    om = OutputManager(configuration)
    tm = TimeManager()

    cc = {}
    for c in controllers:
        ci = c(pm=pm, tm=tm)
        cc[ci.key] = ci.handle

    command = Commands.HELP
    
    if len(options) > 0:
        command = options[0]

    if not command in cc:
        command = Commands.HELP

    options_for_controller = []

    if len(options) > 1:
        options_for_controller = options[1:]

    view = cc[command](options_for_controller)
    om.emmit(view)
