from unittest import TestCase

from forty.tools import ActionsBuilder as A
from forty.common import value_decorator
from forty.managers.project_manager import Config
from forty.reducers import get_total_remained_time


call = value_decorator(get_total_remained_time)
test_config = Config(1, 1)


class TestGetTotalRemainedTime(TestCase):
    def test_default_action_type(self):
        actions = A().test().at().done()

        value = call(actions, test_config)

        self.assertEqual(value, 3600)

    def test_init_action_type(self):
        actions = []

        value = call(actions, test_config)

        self.assertEqual(value, 3600)

    def test_start_action_type(self):
        actions = A().start().at().done()

        value = call(actions, test_config)

        self.assertEqual(value, 3600)

    def test_one_work_interval(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 3590)

    def test_two_work_intervals(self):
        actions = (A()
            .start().at(second=0)
            .finish().at(second=10)
            .start().at(second=20)
            .finish().at(second=30)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, 3580)

    def test_overtime(self):
        actions = (A()
            .start().at(hour=0, second=0)
            .finish().at(hour=1, second=10)
            .done())

        value = call(actions, test_config)

        self.assertEqual(value, -10)
