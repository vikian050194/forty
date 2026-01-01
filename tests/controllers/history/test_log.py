from forty.tools import ActionsBuilder as A
from forty.views import LogView
from forty.controllers.log import LogController

from ..controller_test_case import ControllerTestCase


class TestLogController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return LogController

    def test_no_actions(self):
        view: LogView = self.handle([])

        self.fm.load_project.assert_called_once()
        self.fm.load_actions.assert_called_once()
        self.fm.save_actions.assert_not_called()
        self.assertEqual(view.list, [])

    def test_few_actions(self):
        actions = A().start().finish().done()
        self.actions_to_return(actions)

        view: LogView = self.handle([])

        self.assertEqual(len(view.list), 2)
