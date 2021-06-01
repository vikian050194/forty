from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from forty.command_line import main


class TestCommandLine(TestCase):
    def test_basic(self):
        with patch('sys.stdout', new = StringIO()) as output:
            main()
            self.assertNotEqual(output.getvalue(), '')
