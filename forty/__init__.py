from typing import List

from .controllers import controllers
from .output import OutputManager
from .managers import ProjectManager, TimeManager
from .configuration import Configuration
from .views import StrView


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
        om.emmit(StrView(f"Error. Command is missed. Please try \"help\"."))
        return

    if command in cc:
        view = cc[command](options)
        om.emmit(view)
        return
    else:
        om.emmit(StrView(f"Error. Unknown command \"{command}\". Please try \"help\"."))        
        return
