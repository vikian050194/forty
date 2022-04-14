from unittest import skip

from forty.views import OnlyStatusView, ErrorView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusControllerDefaultCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    @skip("TODO")
    def test_default(self):
        view: OnlyStatusView = self.handle(["status"])

        self.assertEqual(view.status, None)

    def test_last_day_is_not_finished(self):
        actions = A().start().at().done()
        self.now_to_return(day=2)
        self.actions_to_return(actions)

        view: ErrorView = self.handle(["status"])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(self.pm.load_project.call_count, 2)
        self.assertEqual(self.pm.load_actions.call_count, 2)
        self.pm.save_actions.assert_not_called()
        self.assertEqual(view.value, "invalid state at 2021-01-01")
