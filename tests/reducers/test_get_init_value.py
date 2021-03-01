import unittest

from utils import Action, State, Actions, actions_applicator, from_iso
from reducers.get_init_value import get_init_value


call = lambda actions: actions_applicator(get_init_value, actions)


class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        state = call([Action("test", from_iso("2021-01-01T00:00:00"))])

        self.assertEqual(state.value, None)

    def test_init_action_type(self):
        state = call([Action(Actions.INIT, from_iso("2021-01-01T00:00:00"), "40:00:00")])

        self.assertEqual(state.value, "40:00:00")
