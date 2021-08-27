from forty.views.base import ListView
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController

from ..controller_test_case import ControllerTestCase


class TestStatusControllerWhatsupCommand(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusController

    def test_whatsup_started(self):
        self.now_to_return(hour=12, minute=34, second=56)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["04:34:56", "03:25:04", "04:34:56", "35:25:04"])

    def test_whatsup_started_today_overtime(self):
        self.now_to_return(day=1, hour=9, minute=8, second=7)
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["09:08:07", "-01:08:07", "09:08:07", "30:51:53"])

    def test_whatsup_finished_total_overtime(self):
        actions = (A()
            .start().at(day=1,hour=0)
            .finish().at(day=1, hour=23)
            .start().at(day=2,hour=0)
            .finish().at(day=2, hour=23)
            .done())
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["23:00:00", "-15:00:00", "46:00:00", "-06:00:00"])

    def test_whatsup_finished(self):
        self.now_to_return(hour=18, minute=0, second=0)
        actions = A().start().at(hour=8).finish().at(hour=12, minute=34, second=56).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["04:34:56", "03:25:04", "04:34:56", "35:25:04"])
