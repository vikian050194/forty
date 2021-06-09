from typing import List

from .actions import Commands
from .handlers import handlers
from .managers import ProjectManager, OutputManager, TimeManager


def main(home: str, options: List[str], **kwargs):
    pm = ProjectManager(home=home)
    om = OutputManager(**kwargs)
    tm = TimeManager()

    hh = {}
    for h in handlers:
        hi = h(pm=pm, om=om, tm=tm)
        hh[hi.key] = hi.handle

    command = Commands.HELP
    options_for_handler = []

    if len(options) > 0:
        command = options[0]

    if len(options) > 1:
        options_for_handler = options[1:]

    if command in hh:
        hh[command](options_for_handler)
    else:
        hh[Commands.HELP](options_for_handler)
