from typing import List
from forty.controllers.abstract import AbstractController

from forty.controllers.composite import CompositeController

from forty.actions import Commands, StatusOptions
from forty.options import Options
from forty.reducers import *
from forty.models import StatusModel
from forty.views.base import AbstractView


class StatusController(CompositeController):
    def keys(self):
        return [Commands.STATUS]


__all__ = ["StatusController"]
