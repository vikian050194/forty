from unittest import TestCase

from forty.actions import Action, Actions
from forty.common import from_iso, value_decorator
from forty.managers.project_manager import Config
from forty.reducers import get_total_remained_time


call = value_decorator(get_total_remained_time)
test_config = Config(1, 1)


class TestGetTotalRemainedTime(TestCase):
    def test_default_action_type(self):
        value = call([Action("test", from_iso("2021-01-01T00:00:00"))], test_config)

        self.assertEqual(value, 3600)

    def test_init_action_type(self):
        value = call([], test_config)

        self.assertEqual(value, 3600)

    def test_start_action_type(self):
        value = call([Action(Actions.START, from_iso("2021-01-01T00:00:00"))], test_config)

        self.assertEqual(value, 3600)

    def test_one_work_interval(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10"))], test_config)

        self.assertEqual(value, 3590)

    def test_two_work_intervals(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10")),
            Action(Actions.START, from_iso("2021-01-01T00:00:20")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:30"))], test_config)

        self.assertEqual(value, 3580)

    def test_overtime(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T01:00:10"))], test_config)

        self.assertEqual(value, -10)
