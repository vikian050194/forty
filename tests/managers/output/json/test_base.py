from unittest.mock import patch

from forty.views import *

from .case import OutputJsonTestCase

@patch("builtins.print")
class OutputJsonBase(OutputJsonTestCase):
    def test_str(self, mock_print):
        view = StrView("test value")

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "value": "test value"\n}')
        mock_print.reset_mock()

    def test_list(self, mock_print):
        view = ListView(["test", "value", "yeah"])

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('[\n    "test",\n    "value",\n    "yeah"\n]')
        mock_print.reset_mock()
