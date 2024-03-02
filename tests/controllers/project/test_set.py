from forty.views import ErrorView, InfoView
from forty.controllers.project.internal import ProjectSetController

from ..controller_test_case import ControllerTestCase


class TestProjectSetController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectSetController

    def test_wrong_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: ErrorView = self.handle(["ddd"])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(view.value, "project \"ddd\" is not found")

    def test_happy_path(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: InfoView = self.handle(["aaa"])

        self.assertIsInstance(view, InfoView)
        self.assertEqual(view.value, "aaa")
