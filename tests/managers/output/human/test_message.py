from unittest.mock import patch

from forty.views import *

from .case import OutputHumanTestCase


@patch("builtins.print")
class OutputHumanMessage(OutputHumanTestCase):
    def test_info(self, mock_print):
        view = InfoView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("INFO: test value")
        mock_print.reset_mock()

    def test_warning(self, mock_print):
        view = WarningView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("WARNING: test value")
        mock_print.reset_mock()

    def test_error(self, mock_print):
        view = ErrorView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("ERROR: test value")
        mock_print.reset_mock()
