from unittest import TestCase

from forty.actions import Action, Actions
from forty.common import from_iso, value_decorator
from forty.project_manager import Config
from forty.reducers import get_today_remained_time


call = value_decorator(get_today_remained_time)


def get_config(today="2021-01-01"):
    test_config = Config(1, 1)
    test_config.today = today
    return test_config


class TestGetTodayRemainedTime(TestCase):
    def test_default_action_type(self):
        value = call([Action("test", from_iso("2021-01-01T00:00:00"))], get_config())

        self.assertEqual(value, 3600)

    def test_init_action_type(self):
        value = call([], get_config())

        self.assertEqual(value, 3600)

    def test_start_action_type(self):
        value = call([Action(Actions.START, from_iso("2021-01-01T00:00:00"))], get_config())

        self.assertEqual(value, 3600)

    def test_one_work_interval(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10"))], get_config())

        self.assertEqual(value, 3590)

    def test_two_work_intervals(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10")),
            Action(Actions.START, from_iso("2021-01-01T00:00:20")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:30"))], get_config())

        self.assertEqual(value, 3580)

    def test_three_days(self):
        test_today = "2021-01-02"

        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10")),
            Action(Actions.START, from_iso("2021-01-02T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-02T00:00:10")),
            Action(Actions.START, from_iso("2021-01-03T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-03T00:00:10"))], get_config(test_today))

        self.assertEqual(value, 3590)
