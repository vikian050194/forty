from unittest.mock import patch, call

from datetime import datetime

from forty.actions import WorkOptions
from forty.views import *

from .case import OutputHumanTestCase


@patch("builtins.print")
class OutputHumanLog(OutputHumanTestCase):
    def test_one_action(self, mock_print):
        view = LogView([ActionLogView(WorkOptions.START, None, datetime(2022, 4, 24, 9, 0, 17))])

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("start  2022-04-24 09:00:17")
        mock_print.reset_mock()

    def test_two_actions(self, mock_print):
        view = LogView([
            ActionLogView(WorkOptions.START, None, datetime(2022, 4, 24, 9, 0, 17)),
            ActionLogView(WorkOptions.FINISH, None, datetime(2022, 4, 24, 17, 38, 58))
        ])

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 2

        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("start  2022-04-24 09:00:17"))
        self.assertEqual(mock_print.call_args_list[1], call("finish 2022-04-24 17:38:58"))
        mock_print.reset_mock()