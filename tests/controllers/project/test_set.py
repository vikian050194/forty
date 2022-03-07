from forty.views import ErrorView, InfoView
from forty.controllers import ProjectController

from ..controller_test_case import ControllerTestCase


class TestProjectControllerSetCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectController

    def test_wrong_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: ErrorView = self.handle(["project", "set", "ddd"])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(view.value, "project \"ddd\" is not found")

    def test_happy_path(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: InfoView = self.handle(["project", "set", "aaa"])

        self.assertIsInstance(view, InfoView)
        self.assertEqual(view.value, "aaa")
