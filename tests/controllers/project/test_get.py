from unittest import skip
from forty.views import StrView
from forty.controllers import ProjectController

from ..controller_test_case import ControllerTestCase


class TestProjectControllerGetCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectController

    @skip("TODO")
    def test_get_no_current_project(self):
        view: StrView = self.handle(["project", "get"])

        self.assertEqual(view.value, "Error: current project is not specified")

    def test_get(self):
        view: StrView = self.handle(["project", "get"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "test_project")
