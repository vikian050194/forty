from unittest.mock import patch

from forty.views import *

from .case import OutputJsonTestCase


@patch("builtins.print")
class OutputPlainMessage(OutputJsonTestCase):
    def test_info(self, mock_print):
        view = InfoView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "level": "INFO",\n    "value": "test value"\n}')
        mock_print.reset_mock()

    def test_warning(self, mock_print):
        view = WarningView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "level": "WARNING",\n    "value": "test value"\n}')
        mock_print.reset_mock()

    def test_error(self, mock_print):
        view = ErrorView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "level": "ERROR",\n    "value": "test value"\n}')
        mock_print.reset_mock()
