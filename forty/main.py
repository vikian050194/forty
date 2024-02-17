from typing import List

from forty.controllers import controllers
from forty.managers import ProjectManager, TimeManager, OutputManager
from forty.configuration import Configuration
from forty.views import ErrorView
from forty.actions import Commands


def main(options: List[str], configuration: Configuration):
    tm = TimeManager()
    pm = ProjectManager(tm, configuration)
    om = OutputManager(configuration)

    # TODO improve defaults mechanism
    defaults = dict()
    defaults[Commands.STATUS] = configuration.status

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
        if len(options) < 2 and command in defaults:
            options.append(defaults.get(command))
        view = cc[command](options)
        om.emmit(view)
    else:
        om.emmit(ErrorView(f"unknown command \"{command}\", please try \"help\""))

