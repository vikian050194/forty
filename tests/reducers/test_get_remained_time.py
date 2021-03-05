import unittest

from utils import Action, Actions, from_iso, Config
from reducers.get_remained_time import get_remained_time as call


test_config = Config(1, 1)


class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        state = call([Action("test", from_iso("2021-01-01T00:00:00"))], test_config)

        self.assertEqual(state.value, 3600)

    def test_init_action_type(self):
        state = call([], test_config)

        self.assertEqual(state.value, 3600)

    def test_start_action_type(self):
        state = call([Action(Actions.START, from_iso("2021-01-01T00:00:00"))], test_config)

        self.assertEqual(state.value, 3600)

    def test_one_work_interval(self):
        state = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10"))],test_config)

        self.assertEqual(state.value, 3590)

    def test_two_work_intervals(self):
        state = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10")),
            Action(Actions.START, from_iso("2021-01-01T00:00:20")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:30"))], test_config)

        self.assertEqual(state.value, 3580)
