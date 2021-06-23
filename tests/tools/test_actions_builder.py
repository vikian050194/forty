from datetime import datetime
from unittest import TestCase

from forty.actions import Action, Actions
from forty.tools import ActionsBuilder as A


class TestActionsBuilder(TestCase):
    def test_one_start(self):
        expected = [Action(Actions.START, None)]

        actual = A().start().done()

        self.assertEqual(actual, expected)

    def test_two_starts(self):
        expected = [
            Action(Actions.START, None),
            Action(Actions.START, None)]

        actual = A().start().start().done()

        self.assertEqual(actual, expected)

    def test_one_start_at(self):
        expected = [Action(Actions.START, datetime(2021, 1, 1, 12, 34 ,56))]

        actual = A().start().at(hour=12, minute=34, second=56).done()

        self.assertEqual(actual, expected)

    def test_start_and_finish(self):
        expected = [
            Action(Actions.START, None),
            Action(Actions.FINISH, None)]

        actual = A().start().finish().done()

        self.assertEqual(actual, expected)
