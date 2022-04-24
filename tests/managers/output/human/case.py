from unittest import TestCase

from forty.configuration import Configuration, OutputFlagValues
from forty.managers import OutputManager
from forty.views import *


class OutputHumanTestCase(TestCase):
    def setUp(self):
        home="test"
        output=OutputFlagValues.HUMAN
        configuration = Configuration(home=home, output=output)
        om = OutputManager(configuration)

        self.call = lambda view: om.emmit(view)

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
