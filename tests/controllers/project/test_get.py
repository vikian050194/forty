from forty.views import StrView, InfoView
from forty.controllers.project.internal import ProjectGetController

from ..controller_test_case import ControllerTestCase


class TestProjectGetController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectGetController

    def test_get_no_current_project(self):
        self.project_to_return("")

        view: InfoView = self.handle(["project", "get"])

        self.assertIsInstance(view, InfoView)
        self.assertEqual(view.value, "current project is not specified")

    def test_get(self):
        view: StrView = self.handle(["project", "get"])

        self.assertIsInstance(view, StrView)
        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_not_called()
        self.fm.save_actions.assert_not_called()
        self.assertEqual(view.value, "test_project")
