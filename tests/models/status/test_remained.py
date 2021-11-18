from datetime import timedelta, date

from forty.managers.project_manager import Config
from forty.views import RemainedStatusView
from forty.models import StatusModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestStatusModelRemainedMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return StatusModel

    def test_default(self):
        view: RemainedStatusView = self.model.remained()

        self.assertEqual(view.today, timedelta(hours=8))
        self.assertEqual(view.total, timedelta(hours=40))
        
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_today_overtime(self):
        actions = A().start().at(hour=9).finish().at(hour=18).done()
        self.actions_to_return(actions)

        view: RemainedStatusView = self.model.remained()

        self.assertEqual(view.today, timedelta(hours=-1))
        self.assertEqual(view.total, timedelta(hours=31))

    def test_total_overtime(self):
        test_config = Config(day_limit=6, total_limit=8)
        test_config.today = date(year=2021, month=1, day=1)
        self.config_to_return(test_config)

        actions = A().start().at(hour=9).finish().at(hour=18).done()
        self.actions_to_return(actions)

        view: RemainedStatusView = self.model.remained()

        self.assertEqual(view.today, timedelta(hours=-3))
        self.assertEqual(view.total, timedelta(hours=-1))
