from unittest import TestCase, skip
from unittest.mock import patch, call
from tempfile import TemporaryDirectory

from forty.main import main
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
        mock_print.assert_called_with('ERROR: command "not_a_valid_option" is not found, please try "help"')
        mock_print.reset_mock()

    def test_complete_all(self, mock_print):
        complete = ["complete"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 11
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("help")
        mock_print.reset_mock()

# TODO move to unit tests
    def test_complete_project(self, mock_print):
        complete = ["complete", "pr"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("project")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_project_all_subs(self, mock_print):
        complete = ["complete", "project"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 4
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("set")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_project_list(self, mock_print):
        complete = ["complete", "project", "li"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("list")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_project_get(self, mock_print):
        complete = ["complete", "project", "g"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("get")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_project_set(self, mock_print):
        complete = ["complete", "project", "s"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("set")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_project_set_particular(self, mock_print):
        self.call(["project", "new", "test1"])
        mock_print.reset_mock()

        complete = ["complete", "project", "set", "te"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("test1")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_project_new(self, mock_print):
        complete = ["complete", "project", "n"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("new")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status(self, mock_print):
        complete = ["complete", "stat"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("status")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_all_subs(self, mock_print):
        complete = ["complete", "status"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 7
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("total")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_full(self, mock_print):
        complete = ["complete", "status", "f"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("full")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_interval(self, mock_print):
        complete = ["complete", "status", "i"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("interval")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_only(self, mock_print):
        complete = ["complete", "status", "o"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("only")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_passed(self, mock_print):
        complete = ["complete", "status", "p"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("passed")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_remained(self, mock_print):
        complete = ["complete", "status", "r"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("remained")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_today(self, mock_print):
        complete = ["complete", "status", "tod"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("today")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_status_total(self, mock_print):
        complete = ["complete", "status", "tot"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("total")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_start(self, mock_print):
        complete = ["complete", "star"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("start")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_start(self, mock_print):
        complete = ["complete", "fi"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("finish")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_log(self, mock_print):
        complete = ["complete", "l"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("log")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_undo(self, mock_print):
        complete = ["complete", "u"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("undo")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_reset(self, mock_print):
        complete = ["complete", "r"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("reset")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_check(self, mock_print):
        complete = ["complete", "c"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("check")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_date(self, mock_print):
        complete = ["complete", "d"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("date")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_version(self, mock_print):
        complete = ["complete", "v"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("version")
        mock_print.reset_mock()

    # TODO move to unit tests
    def test_complete_help(self, mock_print):
        complete = ["complete", "h"]

        self.call(complete)
        actual_invocations = len(mock_print.call_args_list)
        expected_invocations = 1
        self.assertEqual(actual_invocations, expected_invocations)
        mock_print.assert_called_with("help")
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
