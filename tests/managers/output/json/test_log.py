from unittest.mock import patch, call

from datetime import datetime

from forty.actions import WorkOptions
from forty.views import *

from .case import OutputJsonTestCase

@patch("builtins.print")
class OutputPlainLog(OutputJsonTestCase):
    def test_one_action(self, mock_print):
        view = LogView([ActionLogView(WorkOptions.START, None, datetime(2022, 4, 24, 9, 0, 17))])

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('[\n    {\n        "timestamp": "2022-04-24T09:00:17",\n        "type": "start",\n        "value": null\n    }\n]')
        mock_print.reset_mock()

    def test_two_actions(self, mock_print):
        view = LogView([
            ActionLogView(WorkOptions.START, None, datetime(2022, 4, 24, 9, 0, 17)),
            ActionLogView(WorkOptions.FINISH, None, datetime(2022, 4, 24, 17, 38, 58))
        ])

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('[\n    {\n        "timestamp": "2022-04-24T09:00:17",\n        "type": "start",\n        "value": null\n    },\n    {\n        "timestamp": "2022-04-24T17:38:58",\n        "type": "finish",\n        "value": null\n    }\n]')
        mock_print.reset_mock()
