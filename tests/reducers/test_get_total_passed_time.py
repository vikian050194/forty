from unittest import TestCase

from forty.tools import ActionsBuilder as A
from forty.common import value_decorator
from forty.managers.project_manager import Config
from forty.reducers import get_total_passed_time


call = value_decorator(get_total_passed_time)
test_config = Config(1, 1)


class TestGetTotalPassedTime(TestCase):
    def test_default_action_type(self):
        actions = A().test().at().done()

        value = call(actions, test_config)

        self.assertEqual(value, 0)

    def test_init_action_type(self):
        actions = []

        value = call(actions, test_config)

        self.assertEqual(value, 0)

    def test_start_action_type(self):
        actions = A().start().at().done()

        value = call(actions, test_config)

        self.assertEqual(value, 0)

    def test_one_work_interval(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 10)

    def test_two_work_intervals(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .start().at(second=20)
            .finish().at(second=30)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 20)

    def test_work_almost_24h(self):
        actions = (A()
            .start().at(hour=0, minute=0, second=0)
            .finish().at(hour=23, minute=59, second=59)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 86399)

    def test_work_24h(self):
        actions = (A()
            .start().at(day=1, hour=0, minute=0, second=0)
            .finish().at(day=2, hour=0, minute=0, second=0)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 86400)

    def test_work_almost_48h(self):
        actions = (A()
            .start().at(day=1, hour=0, minute=0, second=0)
            .finish().at(day=2, hour=23, minute=59, second=59)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 172799)
