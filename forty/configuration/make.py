from pathlib import Path
from forty.actions import StatusOptions

from forty.configuration.output import OutputFlagValues

from .configuration import Configuration


def make_config(**kwargs):
    config = Configuration()
    
    home = Path.home().as_posix()
    config._home = kwargs.get("home") or home

    output = OutputFlagValues.HUMAN.value
    config._output = kwargs.get("output") or output

    status = StatusOptions.TODAY.value
    config._status = kwargs.get("status") or status

    return config
