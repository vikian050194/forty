from datetime import timedelta, date
from forty.managers.project_manager import Config
from forty.views import TodayStatusView
from forty.models import StatusModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestStatusModelTodayMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return StatusModel

    def test_no_actions(self):
        view: TodayStatusView = self.model.today()

        self.assertEqual(view.passed, timedelta())
        self.assertEqual(view.remained, timedelta(hours=8))
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_started(self):
        self.now_to_return(hour=13)
        actions = A().start().at(hour=9).done()
        self.actions_to_return(actions)

        view: TodayStatusView = self.model.today()

        self.assertEqual(view.passed, timedelta(hours=4))
        self.assertEqual(view.remained, timedelta(hours=4))

    def test_finished(self):
        self.now_to_return(hour=14)
        actions = A().start().at(hour=9).finish().at(hour=13).done()
        self.actions_to_return(actions)

        view: TodayStatusView = self.model.today()

        self.assertEqual(view.passed, timedelta(hours=4))
        self.assertEqual(view.remained, timedelta(hours=4))

    def test_not_finished_second_day(self):
        test_config = Config(day_limit=8)
        test_config.today = date(year=2021, month=1, day=2)
        self.config_to_return(test_config)
        self.now_to_return(day=2, hour=13)

        actions = (A().start().at(day=1, hour=9)
                .finish().at(day=1, hour=17)
                .start().at(day=2, hour=9)
                .done())
        self.actions_to_return(actions)

        view: TodayStatusView = self.model.today()

        self.assertEqual(view.passed, timedelta(hours=4))
        self.assertEqual(view.remained, timedelta(hours=4))

    def test_finished_second_day(self):
        test_config = Config(day_limit=8)
        test_config.today = date(year=2021, month=1, day=2)
        self.config_to_return(test_config)

        self.now_to_return(day=2, hour=14)

        actions = (A().start().at(day=1, hour=9)
                .finish().at(day=1, hour=17)
                .start().at(day=2, hour=9)
                .finish().at(day=2, hour=13)
                .done())
        self.actions_to_return(actions)

        view: TodayStatusView = self.model.today()

        self.assertEqual(view.passed, timedelta(hours=4))
        self.assertEqual(view.remained, timedelta(hours=4))
