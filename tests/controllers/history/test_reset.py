from forty.views import StrView
from forty.controllers import HistoryController

from ..controller_test_case import ControllerTestCase


class TestHistoryControllerResetCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return HistoryController

    def test_default(self):
        view: StrView = self.handle(["reset"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_not_called()
        self.pm.save_actions.assert_called_once_with([])
        self.assertEqual(view.value, "all actions are deleted")
