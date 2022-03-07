from forty.views import InfoView, WarningView
from forty.controllers import HistoryController

from ..controller_test_case import ControllerTestCase


class TestHistoryControllerUndoCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return HistoryController

    def test_default(self):
        self.actions_to_return(["one", "two", "three"])

        view: InfoView = self.handle(["history", "undo"])

        self.assertIsInstance(view, InfoView)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once_with(["one", "two"])
        self.assertEqual(view.value, "last 1 action is deleted")

    def test_two_actions(self):
        self.actions_to_return(["one", "two", "three"])

        view: InfoView = self.handle(["history", "undo", "2"])

        self.assertIsInstance(view, InfoView)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once_with(["one"])
        self.assertEqual(view.value, "last 2 actions are deleted")

    def test_try_two(self):
        self.actions_to_return(["one"])

        view: WarningView = self.handle(["history", "undo", "2"])

        self.assertIsInstance(view, WarningView)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_called_once_with([])
        self.assertEqual(view.value, "last 1 action is deleted")

    def test_no_actions(self):
        self.actions_to_return([])

        view: WarningView = self.handle(["history", "undo", "2"])

        self.assertIsInstance(view, WarningView)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "no actions are deleted")
