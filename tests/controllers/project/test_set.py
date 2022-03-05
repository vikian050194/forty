from unittest import skip
from forty.views import AbstractView, StrView, ListView
from forty.controllers import ProjectController

from ..controller_test_case import ControllerTestCase


class TestProjectControllerSetCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectController

    def test_set_wrong_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "set", "ddd"])

        self.assertEqual(view.value, "project \"ddd\" is not found")

    def test_set_correct_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "set", "aaa"])

        self.assertEqual(view.value, "aaa")
