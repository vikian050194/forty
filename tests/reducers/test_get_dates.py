from unittest import TestCase

from forty.common import from_iso, value_decorator
from forty.actions import Action, Actions
from forty.reducers import get_dates


call = value_decorator(get_dates)
test_config = None


class TestGetDates(TestCase):
    def test_default_action_type(self):
        value = call([Action("test", from_iso("2021-01-01T00:00:00"))], test_config)

        self.assertEqual(value, [])

    def test_init_action_type(self):
        value = call([], test_config)

        self.assertEqual(value, [])

    def test_start_action_type(self):
        value = call([Action(Actions.START, from_iso("2021-01-01T00:00:00"))], test_config)

        self.assertEqual(value, ["2021-01-01"])

    def test_one_work_interval(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10"))], test_config)

        self.assertEqual(value, ["2021-01-01"])

    def test_two_work_intervals(self):
        value = call([
            Action(Actions.START, from_iso("2021-01-01T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-01T00:00:10")),
            Action(Actions.START, from_iso("2021-01-02T00:00:00")),
            Action(Actions.FINISH, from_iso("2021-01-02T00:00:10"))], test_config)

        self.assertEqual(value, ["2021-01-01", "2021-01-02"])
