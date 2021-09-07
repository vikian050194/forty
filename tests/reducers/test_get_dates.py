from unittest import TestCase

from datetime import date

from forty.tools import ActionsBuilder as A
from forty.common import value_decorator
from forty.reducers import get_dates


call = value_decorator(get_dates)
test_config = None


class TestGetDates(TestCase):
    def test_default_action_type(self):
        actions = A().test().at().done()

        value = call(actions, test_config)

        self.assertEqual(value, [])

    def test_init_action_type(self):
        actions = []

        value = call(actions, test_config)

        self.assertEqual(value, [])

    def test_start_action_type(self):
        actions = A().start().at().done()

        value = call(actions, test_config)

        self.assertEqual(value, [date(2021, 1, 1)])

    def test_one_work_interval(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, [date(2021, 1, 1)])

    def test_two_work_intervals_in_two_days(self):
        actions = (A()
            .start().at(day=1, second=0)
            .finish().at(day=1, second=10)
            .start().at(day=2, second=0)
            .finish().at(day=2, second=10)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, [date(2021, 1, 1), date(2021, 1, 2)])

    def test_two_work_intervals_in_one_day(self):
        actions = (A()
            .start().at(day=1, second=0)
            .finish().at(day=1, second=10)
            .start().at(day=1, second=20)
            .finish().at(day=1, second=30)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, [date(2021, 1, 1)])
