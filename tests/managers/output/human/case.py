from unittest import TestCase

from forty.configuration import make_config, OutputFlagValues
from forty.managers import OutputManager
from forty.views import *


class OutputHumanTestCase(TestCase):
    def setUp(self):
        configuration = make_config(output=OutputFlagValues.HUMAN)
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
