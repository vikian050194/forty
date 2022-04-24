from unittest.mock import patch

from datetime import datetime

from forty.actions import WorkOptions
from forty.views import *

from .test_base import OutputJsonTestCase


@patch("builtins.print")
class OutputPlainAction(OutputJsonTestCase):
    def test_action(self, mock_print):
        view = ActionView(WorkOptions.START, None, datetime(2022, 4, 23, 20, 27, 26))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "timestamp": "2022-04-23T20:27:26",\n    "type": "start",\n    "value": null\n}')
        mock_print.reset_mock()
