from unittest.mock import patch, call

from forty.views import *

from .case import OutputHumanTestCase


@patch("builtins.print")
class OutputHumanBase(OutputHumanTestCase):
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
        expected_invocations = 3

        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("test"))
        self.assertEqual(mock_print.call_args_list[1], call("value"))
        self.assertEqual(mock_print.call_args_list[2], call("yeah"))
        mock_print.reset_mock()
