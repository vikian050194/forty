from unittest import skip

from forty.views import AbstractView
from forty.controllers import ProjectController

from ..controller_test_case import ControllerTestCase


class TestProjectControllerDefaultCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectController

    @skip("TODO")
    def test_default(self):
        view: AbstractView = self.handle(["project"])

        self.pm.load_project.assert_not_called()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_not_called()
        self.assertIsNone(view)
