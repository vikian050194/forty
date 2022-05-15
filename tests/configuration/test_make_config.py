from unittest import skip
from unittest.case import TestCase

from forty.configuration import make_config, Configuration


@skip("TODO")
class TestMakeConfiguration(TestCase):
    def test_no_values(self):
        home = "home"
        output = "human"
        status = "full"

        config = make_config()
        
        self.assertIsInstance(config, Configuration)
        self.assertIsNone(config.home)
        self.assertIsNone(config.output)
        self.assertIsNone(config.status)

    def test_all_values(self):
        home = "home"
        output = "human"
        status = "full"

        config = make_config(home=home, output=output, status=status)
        
        self.assertIsInstance(config, Configuration)
        self.assertEqual(config.home, home)
        self.assertEqual(config.output, output)
        self.assertEqual(config.status, status)