from unittest.mock import patch, call

from datetime import datetime

from forty.actions import WorkOptions
from forty.views import *

from .case import OutputPlainTestCase


@patch("builtins.print")
class OutputPlainBase(OutputPlainTestCase):
    def test_str(self, mock_print):
        view = StrView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("test value")
        mock_print.reset_mock()

    def test_list(self, mock_print):
        view = ListView(["test", "value", "yeah"])

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("test value yeah")
        mock_print.reset_mock()

    def test_action(self, mock_print):
        view = ActionView(WorkOptions.START, None, datetime(2022, 4, 23, 20, 27, 26))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 3

        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("type: start"))
        self.assertEqual(mock_print.call_args_list[1], call("value: None"))
        self.assertEqual(mock_print.call_args_list[2], call("timestamp: 2022-04-23T20:27:26"))
        mock_print.reset_mock()
