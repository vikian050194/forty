import unittest

from utils import Action, Actions, actions_applicator, from_iso
from reducers.get_remained_time import get_remained_time


call = lambda actions: actions_applicator(get_remained_time, actions)


class TestTime(unittest.TestCase):
    def test_default_action_type(self):
        state = call([Action("test", from_iso("2021-01-01T00:00:00"))])

        self.assertEqual(state.value, None)

    def test_init_action_type(self):
        state = call([Action(Actions.INIT, from_iso("2021-01-01T00:00:00"), "40:00:00")])

        self.assertEqual(state.value, "40:00:00")

    def test_start_action_type(self):
        state = call([
            Action(Actions.INIT, from_iso("2021-01-01T00:00:00"), "40:00:00"),
            Action(Actions.START, from_iso("2021-01-01T00:00:00"))])

        self.assertEqual(state.value, "40:00:00")

    def test_one_work_interval(self):
        state = call([
            Action(Actions.INIT, from_iso("2021-01-01T00:00:00"), "40:00:00"),
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.STOP, from_iso("2021-01-01T00:00:10"))])

        self.assertEqual(state.value, "39:59:50")

    def test_two_work_intervals(self):
        state = call([
            Action(Actions.INIT, from_iso("2021-01-01T00:00:00"), "40:00:00"),
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.STOP, from_iso("2021-01-01T00:00:10")),
            Action(Actions.START, from_iso("2021-01-01T00:00:20")),
            Action(Actions.STOP, from_iso("2021-01-01T00:00:30"))])

        self.assertEqual(state.value, "39:59:40")