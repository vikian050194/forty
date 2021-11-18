from forty.actions import Actions
from forty.views.status import OnlyStatusView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusControllerStatusCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_status(self):
        view: OnlyStatusView = self.handle(["status"])

        self.assertEqual(view.status, None)

    def test_status_started(self):
        actions = A().start().done()
        self.actions_to_return(actions)

        view: OnlyStatusView = self.handle(["status"])

        self.assertEqual(view.status, Actions.START)

    def test_status_finished(self):
        actions = A().finish().done()
        self.actions_to_return(actions)

        view: OnlyStatusView = self.handle(["status"])

        self.assertEqual(view.status, Actions.FINISH)
