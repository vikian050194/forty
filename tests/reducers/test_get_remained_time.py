from unittest import TestCase

from forty.actions import Action, Actions
from forty.common import from_iso
from forty.data import Config
from forty.reducers import get_remained_time as call


test_config = Config(1, 1)


class TestGetRemainedTime(TestCase):
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
