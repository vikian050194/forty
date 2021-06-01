from unittest import TestCase, skip
from unittest.mock import patch
from tempfile import TemporaryDirectory

from forty import main


@patch("builtins.print")
class TestMain(TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.home = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @skip("test is not ready")
    def test_foo(self):
        pass

    def test_empty(self, mock_print):
        main(self.home, [])
        
        mock_print.call_args
        mock_print.call_args_list

    @skip("test is not ready")
    def test_help(self, mock_print):
            main(["help"])

    @skip("test is not ready")
    def test_invalid_option(self, mock_print):
            main(["not_a_valid_option"])

    @skip("test is not ready")
    def test_project_list(self, mock_print):
            main(["project", "list"])

    @skip("test is not ready")
    def test_project_get(self, mock_print):
            main(["project", "get"])

    @skip("test is not ready")
    def test_project_set(self, mock_print):
            main(["project", "set", "test_project_1"])

    @skip("test is not ready")
    def test_project_new(self, mock_print):
        main(["project", "new", "test_project_new"])

    @skip("test is not ready")
    def test_start_work(self, mock_print):
            main(["start"])

    @skip("test is not ready")
    def test_finish_work(self, mock_print):
            main(["finish"])

    @skip("test is not ready")
    def test_get_all_available_data(self, mock_print):
            main(["get", "status"])

    @skip("test is not ready")
    def test_get_today_data(self, mock_print):
            # few cases are required?
            main(["get", "today"])

    @skip("test is not ready")
    def test_get_total_data(self, mock_print):
            # few cases are required?
            main(["get", "total"])

    @skip("test is not ready")
    def test_get_passed_data(self, mock_print):
            # few cases are required?
            main(["get", "passed"])

    @skip("test is not ready")
    def test_get_passed_data(self, mock_print):
            # few cases are required?
            main(["get", "remained"])

    @skip("test is not ready")
    def test_get_today_passed_data(self, mock_print):
            # few cases are required?
            main(["get", "today", "passed"])

    @skip("test is not ready")
    def test_get_today_remained_data(self, mock_print):
            # few cases are required?
            main(["get", "today", "remained"])

    @skip("test is not ready")
    def test_get_total_passed_data(self, mock_print):
            # few cases are required?
            main(["get", "total", "passed"])

    @skip("test is not ready")
    def test_get_total_remained_data(self, mock_print):
            # few cases are required?
            main(["get", "total", "remained"])
