from datetime import date

from forty.managers.project_manager import Config
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

        self.assertListEqual(view.list, ["04:34:56", "03:25:04", "04:34:56", "35:25:04", "16:00:00"])

    def test_whatsup_started_today_overtime(self):
        self.now_to_return(day=1, hour=9, minute=8, second=7)
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["09:08:07", "-01:08:07", "09:08:07", "30:51:53", "08:00:00"])

    def test_whatsup_finished_total_overtime(self):
        test_config = Config(day_limit=8, total_limit=40)
        test_config.today = date(year=2021, month=1, day=5)
        self.config_to_return(config=test_config)
        self.now_to_return(day=5, hour=19)
        actions = (A()
            .start().at(day=1,hour=9)
            .finish().at(day=1, hour=17)
            .start().at(day=2,hour=9)
            .finish().at(day=2, hour=17)
            .start().at(day=3,hour=9)
            .finish().at(day=3, hour=17)
            .start().at(day=4,hour=9)
            .finish().at(day=4, hour=17)
            .start().at(day=5,hour=9)
            .finish().at(day=5, hour=18)
            .done())
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["09:00:00", "-01:00:00", "41:00:00", "-01:00:00", None])

    def test_whatsup_finished(self):
        self.now_to_return(hour=18, minute=0, second=0)
        actions = A().start().at(hour=8).finish().at(hour=12, minute=34, second=56).done()
        self.actions_to_return(actions)

        view: ListView = self.handle(["whatsup"])

        self.assertListEqual(view.list, ["04:34:56", "03:25:04", "04:34:56", "35:25:04", None])
