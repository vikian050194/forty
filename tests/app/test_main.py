from unittest import TestCase, skip
from unittest.mock import patch, call
from tempfile import TemporaryDirectory

from forty import main
from forty.configuration import make_config, OutputFlagValues


# @skip("e2e")
@patch("builtins.print")
class TestMain(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        home=self.temp_dir.name
        output=OutputFlagValues.HUMAN
        configuration = make_config(home=home, output=output)
        self.call = lambda options: main(options=options, configuration=configuration)

    def tearDown(self):
        self.temp_dir.cleanup()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_command_is_missed(self, mock_print):
        empty = []

        self.call(empty)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("ERROR: command is missed, please try \"help\"")
        mock_print.reset_mock()

    def test_unknown_command(self, mock_print):
        invalid = ["not_a_valid_option"]

        self.call(invalid)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("ERROR: unknown command \"not_a_valid_option\", please try \"help\"")
        mock_print.reset_mock()

    def test_help(self, mock_print):
        help = ["help"]

        self.call(help)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 3
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.reset_mock()

    def test_project(self, mock_print):
        self.call(["project", "get"])
        mock_print.assert_called_with("INFO: current project is not specified")
        mock_print.reset_mock()

        self.call(["project", "list"])
        mock_print.assert_called_with("INFO: there are no projects")
        mock_print.reset_mock()

        self.call(["project", "new", "aaa"])
        self.call(["project", "list"])
        mock_print.assert_called_with("aaa")
        mock_print.reset_mock()

        self.call(["project", "new", "bbb"])
        self.call(["project", "set", "ccc"])
        mock_print.assert_called_with("ERROR: project \"ccc\" is not found")
        mock_print.reset_mock()
        self.call(["project", "get"])
        mock_print.assert_called_with("bbb")
        mock_print.reset_mock()

        self.call(["project", "set", "aaa"])
        self.call(["project", "get"])
        mock_print.assert_called_with("aaa")
        mock_print.reset_mock()

    @skip("TODO")
    def test_no_project(self, mock_print):
        self.call(["start"])
        mock_print.assert_called_with("error: create")
        mock_print.reset_mock()

        self.call(["finish"])

    def test_status(self, mock_print):
        self.call(["project", "new", "aaa"])
        mock_print.assert_called_with("INFO: aaa")
        mock_print.reset_mock()

        self.call(["status", "full"])
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 7
        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("status:              None"))
        self.assertEqual(mock_print.call_args_list[1], call("today_passed_time:   00:00:00"))
        self.assertEqual(mock_print.call_args_list[2], call("today_remained_time: None"))
        self.assertEqual(mock_print.call_args_list[3], call("total_passed_time:   00:00:00"))
        self.assertEqual(mock_print.call_args_list[4], call("total_remained_time: None"))
        self.assertEqual(mock_print.call_args_list[5], call("from_time:           None"))
        self.assertEqual(mock_print.call_args_list[6], call("to_time:             None"))
        mock_print.reset_mock()

        self.call(["status", "only"])
        mock_print.assert_called_with("status: None")
        mock_print.reset_mock()
        
        self.call(["start", "12:34:56"])
        self.call(["status", "only"])
        mock_print.assert_called_with("status: start")
        mock_print.reset_mock()

        self.call(["finish", "13:00:00"])
        self.call(["status", "only"])
        mock_print.assert_called_with("status: finish")
        mock_print.reset_mock()

        self.call(["status", "full"])
        # TODO: it is not working by some reason
        # self.assertEqual(mock_print.call_args_list[0], call("status: finish"))
        self.assertEqual(mock_print.call_args_list[1], call("today_passed_time:   00:25:04"))
        self.assertEqual(mock_print.call_args_list[2], call("today_remained_time: None"))
        self.assertEqual(mock_print.call_args_list[3], call("total_passed_time:   00:25:04"))
        self.assertEqual(mock_print.call_args_list[4], call("total_remained_time: None"))
        self.assertEqual(mock_print.call_args_list[5], call("from_time:           12:34:56"))
        self.assertEqual(mock_print.call_args_list[6], call("to_time:             None"))
        mock_print.reset_mock()

        self.call(["status", "today"])
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 2
        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("passed:   00:25:04"))
        self.assertEqual(mock_print.call_args_list[1], call("remained: None"))
        mock_print.reset_mock()

        self.call(["status", "total"])
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 2
        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("passed:   00:25:04"))
        self.assertEqual(mock_print.call_args_list[1], call("remained: None"))
        mock_print.reset_mock()

        self.call(["status", "passed"])
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 2
        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("today: 00:25:04"))
        self.assertEqual(mock_print.call_args_list[1], call("total: 00:25:04"))
        mock_print.reset_mock()

        self.call(["status", "remained"])
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 2
        self.assertEqual(actual_invocations, expected_invocations)
        self.assertEqual(mock_print.call_args_list[0], call("today: None"))
        self.assertEqual(mock_print.call_args_list[1], call("total: None"))
        mock_print.reset_mock()

    def test_history_undo(self, mock_print):
        self.call(["project", "new", "test_history"])

        self.call(["start", "12:34:56"])
        self.call(["finish", "13:00:00"])

        self.call(["status", "only"])
        mock_print.assert_called_with("status: finish")
        mock_print.reset_mock()

        self.call(["undo"])

        self.call(["status", "only"])
        mock_print.assert_called_with("status: start")
        mock_print.reset_mock()

        self.call(["undo"])

        self.call(["status", "only"])
        mock_print.assert_called_with("status: None")
        mock_print.reset_mock()

    def test_history_undo(self, mock_print):
        self.call(["project", "new", "test_history"])

        self.call(["start", "12:34:56"])
        self.call(["finish", "13:00:00"])

        self.call(["reset"])
        
        self.call(["status", "only"])
        mock_print.assert_called_with("status: None")
        mock_print.reset_mock()
