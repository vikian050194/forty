from unittest import skip

from forty.views.status import OnlyStatusView
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
