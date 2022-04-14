from typing import List

from .controllers import controllers
from .managers import ProjectManager, TimeManager, OutputManager
from .configuration import Configuration
from .views import ErrorView


def main(options: List[str], configuration: Configuration):
    tm = TimeManager()
    pm = ProjectManager(tm, configuration)
    om = OutputManager(configuration)

    cc = {}
    for c in controllers:
        ci = c(pm=pm, tm=tm)
        for new_key in ci.keys:
            cc[new_key] = ci.handle

    command = None
    
    if len(options) > 0:
        command = options[0]
    else:
        om.emmit(ErrorView(f"command is missed, please try \"help\""))
        return

    if command in cc:
        view = cc[command](options)
        om.emmit(view)
    else:
        om.emmit(ErrorView(f"unknown command \"{command}\", please try \"help\""))

