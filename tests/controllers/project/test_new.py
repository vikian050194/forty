from forty.views import InfoView, ErrorView
from forty.controllers.project.internal import ProjectNewController

from ..controller_test_case import ControllerTestCase


class TestProjectNewController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return ProjectNewController

    def test_missed_name(self):
        view: ErrorView = self.handle([])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(view.value, "new project name is not specified")

    def test_not_unique_name(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: ErrorView = self.handle(["aaa"])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(view.value, "project \"aaa\" could not be created")

    def test_happy_path(self):
        self.projects_to_return(["aaa", "bbb", "ccc"])

        view: InfoView = self.handle(["ddd"])

        self.assertIsInstance(view, InfoView)
        self.assertEqual(view.value, "ddd")
