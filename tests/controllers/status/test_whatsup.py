from datetime import date, time, timedelta

from forty.views.status import FullStatusView
from forty.actions import WorkOptions
from forty.tools import ActionsBuilder as A
from forty.controllers import StatusController
from forty.managers.project_manager import Config

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

        view: FullStatusView = self.handle(["status", "whatsup"])

        self.assertEqual(view.status, WorkOptions.START)
        self.assertEqual(view.today_passed_time, timedelta(hours=4, minutes=34, seconds=56))
        self.assertEqual(view.today_remained_time, timedelta(hours=3, minutes=25, seconds=4))
        self.assertEqual(view.total_passed_time, timedelta(hours=4, minutes=34, seconds=56))
        self.assertEqual(view.total_remained_time, timedelta(hours=35, minutes=25, seconds=4))
        self.assertEqual(view.from_time, time(hour=8))
        self.assertEqual(view.to_time, time(hour=16))

    def test_whatsup_finished(self):
        self.now_to_return(hour=18, minute=0, second=0)
        actions = A().start().at(hour=8).finish().at(hour=12, minute=34, second=56).done()
        self.actions_to_return(actions)

        view: FullStatusView = self.handle(["status", "whatsup"])

        self.assertEqual(view.status, WorkOptions.FINISH)
        self.assertEqual(view.today_passed_time, timedelta(hours=4, minutes=34, seconds=56))
        self.assertEqual(view.today_remained_time, timedelta(hours=3, minutes=25, seconds=4))
        self.assertEqual(view.total_passed_time, timedelta(hours=4, minutes=34, seconds=56))
        self.assertEqual(view.total_remained_time, timedelta(hours=35, minutes=25, seconds=4))
        self.assertEqual(view.from_time, time(hour=8))
        self.assertEqual(view.to_time, None)

    def test_whatsup_started_today_overtime(self):
        self.now_to_return(day=1, hour=9, minute=8, second=7)
        actions = A().start().at().done()
        self.actions_to_return(actions)

        view: FullStatusView = self.handle(["status", "whatsup"])

        self.assertEqual(view.status, WorkOptions.START)
        self.assertEqual(view.today_passed_time, timedelta(hours=9, minutes=8, seconds=7))
        self.assertEqual(view.today_remained_time, timedelta(hours=-1, minutes=-8, seconds=-7))
        self.assertEqual(view.total_passed_time, timedelta(hours=9, minutes=8, seconds=7))
        self.assertEqual(view.total_remained_time, timedelta(hours=30, minutes=51, seconds=53))
        self.assertEqual(view.from_time, time())
        self.assertEqual(view.to_time, time(hour=8))

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

        view: FullStatusView = self.handle(["status", "whatsup"])

        self.assertEqual(view.status, WorkOptions.FINISH)
        self.assertEqual(view.today_passed_time, timedelta(hours=9))
        self.assertEqual(view.today_remained_time, timedelta(hours=-1))
        self.assertEqual(view.total_passed_time, timedelta(hours=41))
        self.assertEqual(view.total_remained_time, timedelta(hours=-1))
        self.assertEqual(view.from_time, time(hour=9))
        self.assertEqual(view.to_time, None)
