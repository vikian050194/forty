from forty.tools import ActionsBuilder as A
from forty.views import LogView
from forty.controllers import HistoryController

from ..controller_test_case import ControllerTestCase


class TestLogController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return HistoryController

    def test_no_actions(self):
        view: LogView = self.handle(["log"])

        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.list, [])

    def test_few_actions(self):
        actions = A().start().finish().done()
        self.actions_to_return(actions)

        view: LogView = self.handle(["log"])

        self.assertEqual(len(view.list), 2)

