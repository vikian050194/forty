from datetime import timedelta
from forty.views.status import RemainedStatusView
from forty.controllers.status.internal import StatusRemainedController

from ..controller_test_case import ControllerTestCase


class TestStatusRemainedController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusRemainedController

    def test_remained(self):
        view: RemainedStatusView = self.handle([])

        self.assertEqual(view.today, timedelta(hours=8))
        self.assertEqual(view.total, timedelta(hours=40))
