from unittest import skip
from forty.views import AbstractView, StrView, ListView
from forty.controllers import ProjectController

from ..controller_test_case import ControllerTestCase


class TestProjectControllerNewCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectController

    @skip("TODO")
    def test_new_missed_name(self):
        view: StrView = self.handle(["project", "new"])

        self.assertEqual(view.value, "Error: new project name is not specified")

    def test_new_not_unique_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "new", "aaa"])

        self.assertEqual(view.value, "project \"aaa\" could not be (re)created")

    def test_new(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: StrView = self.handle(["project", "new", "ddd"])

        self.assertEqual(view.value, "ddd")
