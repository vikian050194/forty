import unittest

from utils import Action, Actions, from_iso
from reducers.get_current_status import get_current_status as call


class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        state = call([Action("test")])

        self.assertEqual(state.value, None)

    def test_init_action_type(self):
        state = call([Action(Actions.START)])

        self.assertEqual(state.value, Actions.START)

    def test_start_action_type(self):
        state = call([
            Action(Actions.START),
            Action(Actions.FINISH)])

        self.assertEqual(state.value, Actions.FINISH)
        
    def test_start_action_type(self):
        state = call([
            Action(Actions.START),
            Action(Actions.FINISH),
            Action(Actions.START),
            Action(Actions.FINISH)])

        self.assertEqual(state.value, Actions.FINISH)
