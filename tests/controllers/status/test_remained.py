from forty.views.base import ListView
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
        view: ListView = self.handle(["remained"])

        self.assertListEqual(view.list, ["08:00:00", "40:00:00"])
