from unittest import TestCase

from forty.common import from_iso
from forty.actions import Action, Actions
from forty.reducers import get_current_status as call


class TestGetCurrentStatus(TestCase):
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
