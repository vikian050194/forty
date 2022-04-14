from datetime import timedelta

from forty.views import TotalStatusView, ErrorView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_total(self):
        view: TotalStatusView = self.handle(["status", "total"])

        self.assertEqual(view.passed, timedelta())
        self.assertEqual(view.remained, timedelta(hours=40))

    def test_total_started(self):
        self.now_to_return(hour=19, minute=33, second=42)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        view: TotalStatusView = self.handle(["status", "total"])

        self.assertEqual(view.passed, timedelta(hours=10, minutes=33, seconds=42))
        self.assertEqual(view.remained, timedelta(hours=29, minutes=26, seconds=18))

    def test_total_started_overtime(self):
        self.now_to_return(day=3,hour=3, minute=4, second=5)
        actions = A().start().at(day=1, hour=8).done()
        self.actions_to_return(actions)

        view: ErrorView = self.handle(["status", "total"])

        self.assertIsInstance(view, ErrorView)
        self.assertEqual(view.value, "invalid state at 2021-01-01")
