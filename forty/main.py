from typing import List
from forty.controllers.check import CheckController

from forty.controllers.composite import CompositeController
from forty.controllers.date import DateController
from forty.controllers.finish import FinishController
from forty.controllers.help import HelpController
from forty.controllers.log import LogController
from forty.controllers.project import *
from forty.controllers.reset import ResetController
from forty.controllers.start import StartController
from forty.controllers.status import *
from forty.controllers.undo import UndoController
from forty.controllers.version import VersionController
from forty.managers import ProjectManager, TimeManager, OutputManager
from forty.configuration import Configuration
from forty.options import Options
from forty.actions import Commands


def main(options: List[str], configuration: Configuration):
    tm = TimeManager()
    pm = ProjectManager(tm, configuration)
    om = OutputManager(configuration)

    # TODO improve defaults mechanism
    defaults = dict()
    defaults[Commands.STATUS] = configuration.status

    project_subs = [
        ProjectListController(pm, tm),
        ProjectNewController(pm, tm),
        ProjectGetController(pm, tm),
        ProjectSetController(pm, tm)
    ]
    project_controller = ProjectController(pm, tm, project_subs)

    status_subs = [
        StatusFullController(pm, tm),
        StatusIntervalController(pm, tm),
        StatusOnlyController(pm, tm),
        StatusPassedController(pm, tm),
        StatusRemainedController(pm, tm),
        StatusTodayController(pm, tm),
        StatusTotalController(pm, tm)
    ]
    status_controller = StatusController(pm, tm, status_subs)

    start_controller = StartController(pm, tm)
    finish_controller = FinishController(pm, tm)

    # TODO probably following 5 controllers should be behind single composite controller
    log_controller = LogController(pm, tm)
    undo_controller = UndoController(pm, tm)
    reset_controller = ResetController(pm, tm)
    check_controller = CheckController(pm, tm)
    date_controller = DateController(pm, tm)

    version_controller = VersionController(pm, tm)

    help_controller = HelpController(pm, tm)

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

    root_controller = CompositeController(pm, tm, controllers)

    command = None
    
    if len(options) > 0:
        command = options[0]

    opt = Options(values=options, complete=False)

    if command == "complete":
        command = options[1] if len(options) > 1 else None
        opt = Options(values=options[1:], complete=True)

    if len(opt.values) < 2 and command in defaults:
        opt.values.append(defaults.get(command))
    view = root_controller.handle(opt)
    om.emmit(view)
