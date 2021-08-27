from forty.views.base import StrView, ListView
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
        view: StrView = self.handle(["status"])

        self.assertEqual(view.value, "none")

    def test_status_started(self):
        actions = A().start().done()
        self.actions_to_return(actions)

        view: StrView = self.handle(["status"])

        self.assertEqual(view.value, "start")

    def test_status_finished(self):
        actions = A().finish().done()
        self.actions_to_return(actions)

        view: StrView = self.handle(["status"])

        self.assertEqual(view.value, "finish")
