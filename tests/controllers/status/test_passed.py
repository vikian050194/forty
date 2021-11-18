from datetime import timedelta

from forty.views.status import PassedStatusView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusControllerPassedCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_passed(self):
        view: PassedStatusView = self.handle(["passed"])

        self.assertEqual(view.today, timedelta())
        self.assertEqual(view.total, timedelta())
