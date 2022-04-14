from typing import List

from datetime import date

from forty.models import HistoryModel
from forty.tools import ActionsBuilder as A

from ..model_test_case import ModelTestCase


class TestHistoryModelDateMethod(ModelTestCase):
    def __init__(self, *args, **kwargs):
        ModelTestCase.__init__(self, *args, **kwargs)

    @property
    def model_class(self):
        return HistoryModel

    def test_no_actions(self):
        self.actions_to_return([])

        result: List[date] = self.model.date()

        self.assertEqual(result, [])
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_one_day(self):
        actions = A().start().at(day=1).finish().at(day=1).done()
        self.actions_to_return(actions)

        result: List[date] = self.model.date()

        self.assertEqual(result, [date(year=2021, month=1, day=1)])
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()

    def test_two_days(self):
        actions = (A()
            .start().at(day=1)
            .finish().at(day=1)
            .start().at(day=2)
            .finish().at(day=2)
            .done())
        self.actions_to_return(actions)

        result: List[date] = self.model.date()

        self.assertEqual(result, [
            date(year=2021, month=1, day=1),
            date(year=2021, month=1, day=2)])
        self.pm.load_project.assert_called_once()
        self.pm.load_actions.assert_called_once()
