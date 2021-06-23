from unittest import TestCase

from forty.common import value_decorator
from forty.tools import ActionsBuilder as A
from forty.actions import Actions
from forty.reducers import get_current_status


call = value_decorator(get_current_status)


class TestGetCurrentStatus(TestCase):
    def test_default_action_type(self):
        actions = A().test().done()

        value = call(actions)

        self.assertEqual(value, None)

    def test_only_start_action(self):
        actions = A().start().done()

        value = call(actions)

        self.assertEqual(value, Actions.START)

    def test_one_interval(self):
        actions = A().start().finish().done()

        value = call(actions)

        self.assertEqual(value, Actions.FINISH)
        
    def test_two_intervals(self):
        actions = A().start().finish().start().finish().done()

        value = call(actions)

        self.assertEqual(value, Actions.FINISH)
