from datetime import date

from forty.models import HistoryModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestHistoryModelCheckMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return HistoryModel

    def test_one_day_no_actions(self):
        self.actions_to_return([])

        result: bool = self.model.check(date(year=2021, month=1, day=1))

        self.assertTrue(result)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_one_day_not_finished(self):
        actions = A().start().at(day=1).done()
        self.actions_to_return(actions)

        result: bool = self.model.check(date(year=2021, month=1, day=1))

        self.assertFalse(result)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_one_day_finished(self):
        actions = A().start().at(day=1).finish().at(day=1).done()
        self.actions_to_return(actions)

        result: bool = self.model.check(date(year=2021, month=1, day=1))

        self.assertTrue(result)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_one_day_two_finish(self):
        actions = (A()
            .start().at(day=1)
            .finish().at(day=1)
            .start().at(day=1)
            .finish().at(day=1)
            .done())
        self.actions_to_return(actions)

        result: bool = self.model.check(date(year=2021, month=1, day=1))

        self.assertTrue(result)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_one_day_out_of_two_days(self):
        actions = (A()
            .start().at(day=1)
            .finish().at(day=1)
            .start().at(day=2)
            .finish().at(day=2)
            .done())
        self.actions_to_return(actions)

        result: bool = self.model.check(date(year=2021, month=1, day=2))

        self.assertTrue(result)
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
