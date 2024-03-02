from datetime import timedelta

from forty.views.status import PassedStatusView
from forty.controllers.status.internal import StatusPassedController

from ..controller_test_case import ControllerTestCase


class TestStatusPassedController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusPassedController

    def test_passed(self):
        view: PassedStatusView = self.handle([])

        self.assertEqual(view.today, timedelta())
        self.assertEqual(view.total, timedelta())
