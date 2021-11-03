from unittest import TestCase

from datetime import date

from forty.tools import ActionsBuilder as A
from forty.common import value_decorator
from forty.managers.project_manager import Config
from forty.reducers import get_today_remained_time


call = value_decorator(get_today_remained_time)


def get_config(year=2021, month=1, day=1):
    today = date(year, month, day)
    test_config = Config(1, 1)
    test_config.today = today
    return test_config


class TestGetTodayRemainedTime(TestCase):
    def test_default_action_type(self):
        actions = A().test().at().done()

        value = call(actions, get_config())

        self.assertEqual(value, 3600)

    def test_init_action_type(self):
        actions = []

        value = call(actions, get_config())

        self.assertEqual(value, 3600)

    def test_start_action_type(self):
        actions = A().start().at().done()

        value = call(actions, get_config())

        self.assertEqual(value, 3600)

    def test_one_work_interval(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .done())

        value = call(actions, get_config())

        self.assertEqual(value, 3590)

    def test_two_work_intervals(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .start().at(second=20)
            .finish().at(second=30)
            .done())

        value = call(actions, get_config())

        self.assertEqual(value, 3580)

    def test_three_days(self):
        test_day = 2

        actions = (A()
            .start().at(day=1, second=0)
            .finish().at(day=1, second=10)
            .start().at(day=2, second=0)
            .finish().at(day=2, second=10)
            .start().at(day=3, second=0)
            .finish().at(day=3, second=10)
            .done())

        value = call(actions, get_config(day=test_day))

        self.assertEqual(value, 3590)

    def test_overtime(self):
        test_day = 1

        actions = (A()
            .start().at(hour=0, minute=0, second=0)
            .finish().at(hour=2, minute=3, second=4)
            .done())

        value = call(actions, get_config(day=test_day))

        self.assertEqual(value, -3784)
