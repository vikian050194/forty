import unittest

from utils import Action, State

from reducers.get_init_value import get_init_value

class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        test_action = Action("test", "2021-01-01T00:00:00")

        state = get_init_value(None, test_action)

        self.assertEqual(state.value, None)

    def test_init_action_type(self):
        test_action = Action("init", "2021-01-01T00:00:00", "40:00:00")

        state = get_init_value(None, test_action)

        self.assertEqual(state.value, "40:00:00")
