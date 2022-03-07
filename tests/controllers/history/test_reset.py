from forty.views import InfoView
from forty.controllers import HistoryController

from ..controller_test_case import ControllerTestCase


class TestHistoryControllerResetCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return HistoryController

    def test_default(self):
        self.actions_to_return(["first", "second", "third"])

        view: InfoView = self.handle(["history", "reset"])

        self.assertIsInstance(view, InfoView)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_called_once_with([])
        self.assertEqual(view.value, "all actions are deleted")

    def test_no_actions(self):
        self.actions_to_return([])

        view: InfoView = self.handle(["history", "reset"])

        self.assertIsInstance(view, InfoView)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_called_once_with([])
        self.assertEqual(view.value, "all actions are deleted")
