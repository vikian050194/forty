from unittest import TestCase, skip
from unittest.mock import patch, call
from tempfile import TemporaryDirectory

from forty import main
from forty.configuration import Configuration, OutputFlagValues


# @skip("e2e")
@patch("builtins.print")
class TestMain(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        home=self.temp_dir.name
        output=OutputFlagValues.HUMAN
        configuration = Configuration(home=home, output=output)
        self.call = lambda options: main(options=options, configuration=configuration)

    def tearDown(self):
        self.temp_dir.cleanup()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @skip("foo")
    def test_model(self):
        pass

    # @skip("ready")
    def test_help(self, mock_print):
        empty = []
        invalid = ["not_a_valid_option"]
        help = ["help"]
        cases = [empty, invalid, help]

        for case in cases:
            self.call(case)
            actual_invocations = len(mock_print.call_args_list)
            expected_invocations = 6
            self.assertEqual(actual_invocations, expected_invocations)
            mock_print.reset_mock()

    # @skip("ready")
    def test_project(self, mock_print):
        self.call(["project", "get"])
        mock_print.assert_called_with("")
        mock_print.reset_mock()

        self.call(["project", "list"])
        mock_print.assert_not_called()
        mock_print.reset_mock()

        self.call(["project", "new", "aaa"])
        self.call(["project", "list"])
        mock_print.assert_called_with("aaa")
        mock_print.reset_mock()

        self.call(["project", "new", "bbb"])
        self.call(["project", "set", "ccc"])
        mock_print.assert_has_calls([call("aaa"), call("bbb")])
        mock_print.reset_mock()
        self.call(["project", "get"])
        mock_print.assert_called_with("bbb")
        mock_print.reset_mock()

        self.call(["project", "set", "aaa"])
        self.call(["project", "get"])
        mock_print.assert_called_with("aaa")
        mock_print.reset_mock()

    @skip("test is not ready")
    def test_no_project(self, mock_print):
        self.call(["start"])
        mock_print.assert_called_with("error: create")
        mock_print.reset_mock()

        self.call(["finish"])

    # @skip("ready")
    def test_get(self, mock_print):
        self.call(["project", "new", "aaa"])
        mock_print.assert_called_with("aaa")
        mock_print.reset_mock()

        self.call(["get"])
        mock_print.assert_called_with("aaa/none/00:00:00/00:00:00")
        mock_print.reset_mock()

        self.call(["get", "status"])
        mock_print.assert_called_with("aaa/none")
        mock_print.reset_mock()
        
        self.call(["start", "12:34:56"])
        self.call(["get", "status"])
        mock_print.assert_called_with("aaa/started")
        mock_print.reset_mock()

        self.call(["finish", "13:00:00"])
        self.call(["get", "status"])
        mock_print.assert_called_with("aaa/finished")
        mock_print.reset_mock()

        self.call(["get"])
        mock_print.assert_called_with("aaa/finished/00:25:04/00:25:04")
        mock_print.reset_mock()

        self.call(["get", "today"])
        mock_print.assert_called_with("aaa/finished/00:25:04")
        mock_print.reset_mock()

        self.call(["get", "total"])
        mock_print.assert_called_with("aaa/finished/00:25:04")
        mock_print.reset_mock()

        self.call(["get", "passed"])
        mock_print.assert_called_with("aaa/finished/00:25:04/00:25:04")
        mock_print.reset_mock()

        self.call(["get", "remained"])
        mock_print.assert_called_with("aaa/finished")
        mock_print.reset_mock()
