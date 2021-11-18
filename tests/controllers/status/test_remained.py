from datetime import timedelta
from forty.views.status import RemainedStatusView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusControllerRemainedCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_remained(self):
        view: RemainedStatusView = self.handle(["remained"])

        self.assertEqual(view.today, timedelta(hours=8))
        self.assertEqual(view.total, timedelta(hours=40))
