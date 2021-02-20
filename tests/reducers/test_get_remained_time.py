import unittest

from utils import Action

from reducers.get_remained_time import get_remained_time

class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        test_action = Action("test", "2021-01-01T00:00:00")

        state = get_remained_time(None, test_action)

        self.assertEqual(state.value, None)

    def test_init_action_type(self):
        test_action = Action("init", "2021-01-01T00:00:00", "40:00:00")

        state = get_remained_time(None, test_action)

        self.assertEqual(state.value, "40:00:00")
