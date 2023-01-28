from io import StringIO
from unittest import TestCase, skip
from unittest.mock import patch

from forty import app


class TestCommandLine(TestCase):
    def test_basic(self):
        with patch('sys.stdout', new = StringIO()) as view:
            app.run()
            self.assertFalse("Traceback" in view.getvalue())
