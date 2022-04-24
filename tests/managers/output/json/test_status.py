from unittest.mock import patch, call

from datetime import time, timedelta

from forty.actions import WorkOptions
from forty.views import *

from .case import OutputJsonTestCase


@patch("builtins.print")
class OutputPlainStatus(OutputJsonTestCase):
    def test_today(self, mock_print):
        view = TodayStatusView(time(8, 9, 10), time(12, 23, 14))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "passed": "08:09:10",\n    "remained": "12:23:14"\n}')
        mock_print.reset_mock()

    def test_total(self, mock_print):
        view = TotalStatusView(time(8, 9, 10), time(12, 23, 14))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "passed": "08:09:10",\n    "remained": "12:23:14"\n}')
        mock_print.reset_mock()

    def test_passed(self, mock_print):
        view = PassedStatusView(time(8, 9, 10), time(12, 23, 14))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "today": "08:09:10",\n    "total": "12:23:14"\n}')
        mock_print.reset_mock()

    def test_remained(self, mock_print):
        view = RemainedStatusView(time(8, 9, 10), time(12, 23, 14))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "today": "08:09:10",\n    "total": "12:23:14"\n}')
        mock_print.reset_mock()

    def test_interval(self, mock_print):
        view = IntervalStatusView(time(8, 9, 10), time(12, 23, 14))

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "from_time": "08:09:10",\n    "to_time": "12:23:14"\n}')
        mock_print.reset_mock()

    def test_status(self, mock_print):
        view = OnlyStatusView(WorkOptions.START)

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "status": "start"\n}')
        mock_print.reset_mock()

    def test_full(self, mock_print):
        view = FullStatusView()
        view.status = WorkOptions.FINISH
        view.today_passed_time = timedelta(hours=4, minutes=5, seconds=6)
        view.today_remained_time = timedelta(hours=3, minutes=2, seconds=1)
        view.total_passed_time = timedelta(hours=24, minutes=25, seconds=26)
        view.total_remained_time = timedelta(hours=7, minutes=8, seconds=9)
        view.from_time = time(8, 9, 10)
        view.to_time = time(18, 30, 0)

        self.call(view)

        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1

        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with('{\n    "from_time": "08:09:10",\n    "status": "finish",\n    "to_time": "18:30:00",\n    "today_passed_time": "04:05:06",\n    "today_remained_time": "03:02:01",\n    "total_passed_time": "24:25:26",\n    "total_remained_time": "07:08:09"\n}')
        mock_print.reset_mock()
