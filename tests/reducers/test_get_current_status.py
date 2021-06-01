from unittest import TestCase

from forty.common import from_iso, value_decorator
from forty.actions import Action, Actions
from forty.reducers import get_current_status


call = value_decorator(get_current_status)


class TestGetCurrentStatus(TestCase):
    def test_default_action_type(self):
        value = call([Action("test")])

        self.assertEqual(value, None)

    def test_only_start_action(self):
        value = call([Action(Actions.START)])

        self.assertEqual(value, Actions.START)

    def test_one_interval(self):
        value = call([
            Action(Actions.START),
            Action(Actions.FINISH)])

        self.assertEqual(value, Actions.FINISH)
        
    def test_two_intervals(self):
        value = call([
            Action(Actions.START),
            Action(Actions.FINISH),
            Action(Actions.START),
            Action(Actions.FINISH)])

        self.assertEqual(value, Actions.FINISH)
