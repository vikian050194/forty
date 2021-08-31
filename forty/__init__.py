from typing import List

from .actions import Commands
from .controllers import controllers
from .managers import ProjectManager, OutputManager, TimeManager
from .configuration import Configuration


def main(options: List[str], configuration: Configuration):
    tm = TimeManager()
    pm = ProjectManager(tm, configuration)
    om = OutputManager(configuration)

    cc = {}
    for c in controllers:
        ci = c(pm=pm, tm=tm)
        for new_key in ci.keys:
            cc[new_key] = ci.handle

    command = Commands.HELP
    
    if len(options) > 0:
        command = options[0]

    if not command in cc:
        command = Commands.HELP

    view = cc[command](options)
    om.emmit(view)
