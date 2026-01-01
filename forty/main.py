from typing import List

from forty.controllers.check import CheckController
from forty.controllers.composite import CompositeController
from forty.controllers.date import DateController
from forty.controllers.finish import FinishController
from forty.controllers.help import HelpController
from forty.controllers.log import LogController
from forty.controllers.project import ProjectController
from forty.controllers.reset import ResetController
from forty.controllers.start import StartController
from forty.controllers.status import StatusController
from forty.controllers.undo import UndoController
from forty.controllers.version import VersionController
from forty.managers import FileManager, TimeManager, OutputManager
from forty.configuration import Configuration
from forty.options import Options
from forty.actions import Commands


def main(options: List[str], configuration: Configuration):
    tm = TimeManager()
    fm = FileManager(tm, configuration)
    om = OutputManager(configuration)

    # TODO improve defaults mechanism
    defaults = dict()
    defaults[Commands.STATUS] = configuration.status

    project_controller = ProjectController(fm, tm)

    status_controller = StatusController(fm, tm)

    start_controller = StartController(fm, tm)
    finish_controller = FinishController(fm, tm)

    # TODO probably following 5 controllers should be behind single composite controller
    log_controller = LogController(fm, tm)
    undo_controller = UndoController(fm, tm)
    reset_controller = ResetController(fm, tm)
    check_controller = CheckController(fm, tm)
    date_controller = DateController(fm, tm)

    version_controller = VersionController(fm, tm)

    help_controller = HelpController(fm, tm)

    controllers = [
        project_controller,
        status_controller,
        start_controller,
        finish_controller,
        log_controller,
        undo_controller,
        reset_controller,
        check_controller,
        date_controller,
        version_controller,
        help_controller
    ]

    root_controller = CompositeController(fm, tm, controllers)

    command = None
    
    if len(options) > 0:
        command = options[0]

    opt = Options(values=options, complete=False)

    if command == "complete":
        command = options[1] if len(options) > 1 else None
        opt = Options(values=options[1:], complete=True)
    else:
        if len(opt.values) < 2 and command in defaults:
            opt.values.append(defaults.get(command))
    view = root_controller.handle(opt)
    om.emmit(view)
