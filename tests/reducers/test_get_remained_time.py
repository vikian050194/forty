import unittest

from utils import Action, Actions, actions_applicator
from reducers.get_remained_time import get_remained_time


call = lambda actions: actions_applicator(get_remained_time, actions)


class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        state = call([Action("test", "2021-01-01T00:00:00")])

        self.assertEqual(state.value, None)

    def test_init_action_type(self):
        state = call([Action(Actions.INIT, "2021-01-01T00:00:00", "40:00:00")])

        self.assertEqual(state.value, "40:00:00")

    def test_start_action_type(self):
        state = call([
            Action(Actions.INIT, "2021-01-01T00:00:00", "40:00:00"),
            Action(Actions.START, "2021-01-01T00:00:00")])

        self.assertEqual(state.value, "40:00:00")

    def test_one_work_iteration(self):
        state = call([
            Action(Actions.INIT, "2021-01-01T00:00:00", "40:00:00"),
            Action(Actions.START, "2021-01-01T00:00:00"),
            Action(Actions.STOP, "2021-01-01T00:00:10")])

        self.assertEqual(state.value, "39:59:50")
