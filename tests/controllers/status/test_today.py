from unittest.case import skip

from datetime import date, timedelta

from forty.views.status import TodayStatusView
from forty.tools import ActionsBuilder as A
from forty.controllers.status.internal import StatusTodayController
from forty.managers.file_manager import Config

from ..controller_test_case import ControllerTestCase


class TestStatusTodayController(ControllerTestCase):
    def __init__(self, *args, **kwargs):
        ControllerTestCase.__init__(self, *args, **kwargs)

    @property
    def controller_class(self):
        return StatusTodayController

    def test_today_started(self):
        self.now_to_return(hour=14, minute=15, second=16)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        view: TodayStatusView = self.handle([])

        self.assertEqual(view.passed, timedelta(hours=6, minutes=15, seconds=16))
        self.assertEqual(view.remained, timedelta(hours=1, minutes=44, seconds=44))


    def test_today_started_overtime(self):
        self.now_to_return(hour=16, minute=17, second=18)
        actions = A().start().at(hour=8).done()
        self.actions_to_return(actions)

        view: TodayStatusView = self.handle([])

        # TODO refactoring: negative timedelta is looking a bit weird
        self.assertEqual(view.passed, timedelta(hours=8, minutes=17, seconds=18))
        self.assertEqual(view.remained, timedelta(hours=0, minutes=-17, seconds=-18))

    @skip("TODO: change this behavior")
    def test_started_yesterday(self):
        self.now_to_return(day=2, hour=3, minute=4, second=5)
        config = Config(day_limit=8, total_limit=40)
        config.today = date(2021, 1, 2)
        self.config_to_return(config)
        actions = A().start().at(day=1).done()
        self.actions_to_return(actions)

        view: TodayStatusView = self.handle([])

        self.assertEqual(view.passed, timedelta(hours=3, minutes=4, seconds=5))
        self.assertEqual(view.remained, timedelta(hours=4, minutes=55, seconds=55))
