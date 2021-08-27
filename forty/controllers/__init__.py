from typing import List

from .base import *
from .help import *
from .status import *
from .project import *
from .work import *
from .history import *


controllers: List[AbstractController] = [
    HelpController,
    StatusController,
    ProjectController,
    WorkController,
    HistoryController
]


__all__ = ["controllers"]
