from forty.views.base import ListView
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
        view: ListView = self.handle(["total"])

        self.assertListEqual(view.list, ["00:00:00", "40:00:00"])

    def test_total_started(self):
        self.now_to_return(hour=19, minute=33, second=42)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["total"])

        self.assertListEqual(view.list, ["10:33:42", "29:26:18"])

    def test_total_started_overtime(self):
        self.now_to_return(day=3,hour=3, minute=4, second=5)
        actions = A().start().at(day=1, hour=8).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["total"])

        self.assertListEqual(view.list, ["43:04:05", "-03:04:05"])
