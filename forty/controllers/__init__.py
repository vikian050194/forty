from typing import List

from .base import *
from .help import *
from .status import *
from .project import *
from .work import *
from .history import *
from .log import *


controllers: List[AbstractController] = [
    HelpController,
    StatusController,
    ProjectController,
    WorkController,
    HistoryController,
    LogController
]


__all__ = ["controllers"]
