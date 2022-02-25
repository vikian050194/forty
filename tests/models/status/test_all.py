from datetime import time, date, timedelta
from forty.managers.project_manager import Config
from forty.views import StatusView
from forty.models import StatusModel
from forty.tools import ActionsBuilder as A
from forty.actions import WorkOptions

from ..model_test_case import ModelTestCase


class TestStatusModelIntervalMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return StatusModel

    def test_no_actions(self):
        view: StatusView = self.model.all()

        self.assertEqual(view.status, None)
        self.assertEqual(view.today_passed_time, timedelta())
        self.assertEqual(view.today_remained_time, timedelta(hours=8))
        self.assertEqual(view.total_passed_time, timedelta())
        self.assertEqual(view.total_remained_time, timedelta(hours=40))
        self.assertEqual(view.from_time, None)
        self.assertEqual(view.to_time, None)
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_started(self):
        self.now_to_return(hour=13)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        view: StatusView = self.model.all()

        self.assertEqual(view.status, WorkOptions.START)
        self.assertEqual(view.today_passed_time, timedelta(hours=4))
        self.assertEqual(view.today_remained_time, timedelta(hours=4))
        self.assertEqual(view.total_passed_time, timedelta(hours=4))
        self.assertEqual(view.total_remained_time, timedelta(hours=36))
        self.assertEqual(view.from_time, time(hour=9))
        self.assertEqual(view.to_time, time(hour=17))

    def test_finished(self):
        self.now_to_return(hour=14)
        actions = A().start().at(hour=9).finish().at(hour=13).done()
        self.actions_to_return(actions)

        view: StatusView = self.model.all()

        self.assertEqual(view.status, WorkOptions.FINISH)
        self.assertEqual(view.today_passed_time, timedelta(hours=4))
        self.assertEqual(view.today_remained_time, timedelta(hours=4))
        self.assertEqual(view.total_passed_time, timedelta(hours=4))
        self.assertEqual(view.total_remained_time, timedelta(hours=36))
        self.assertEqual(view.from_time, time(hour=9))
        self.assertEqual(view.to_time, None)

    def test_not_finished_second_day(self):
        test_config = Config(day_limit=8, total_limit=40)
        test_config.today = date(year=2021, month=1, day=2)
        self.config_to_return(test_config)
        self.now_to_return(day=2, hour=13)

        actions = (A().start().at(day=1, hour=9)
                .finish().at(day=1, hour=17)
                .start().at(day=2, hour=9)
                .done())
        self.actions_to_return(actions)

        view: StatusView = self.model.all()

        self.assertEqual(view.status, WorkOptions.START)
        self.assertEqual(view.today_passed_time, timedelta(hours=4))
        self.assertEqual(view.today_remained_time, timedelta(hours=4))
        self.assertEqual(view.total_passed_time, timedelta(hours=12))
        self.assertEqual(view.total_remained_time, timedelta(hours=28))
        self.assertEqual(view.from_time, time(hour=9))
        self.assertEqual(view.to_time, time(hour=17))

    def test_finished_second_day(self):
        test_config = Config(day_limit=8, total_limit=40)
        test_config.today = date(year=2021, month=1, day=2)
        self.config_to_return(test_config)

        self.now_to_return(day=2, hour=14)

        actions = (A().start().at(day=1, hour=9)
                .finish().at(day=1, hour=17)
                .start().at(day=2, hour=9)
                .finish().at(day=2, hour=13)
                .done())
        self.actions_to_return(actions)

        view: StatusView = self.model.all()

        self.assertEqual(view.status, WorkOptions.FINISH)
        self.assertEqual(view.today_passed_time, timedelta(hours=4))
        self.assertEqual(view.today_remained_time, timedelta(hours=4))
        self.assertEqual(view.total_passed_time, timedelta(hours=12))
        self.assertEqual(view.total_remained_time, timedelta(hours=28))
        self.assertEqual(view.from_time, time(hour=9))
        self.assertEqual(view.to_time, None)

