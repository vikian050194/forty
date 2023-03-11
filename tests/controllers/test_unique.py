from unittest.case import TestCase

from .controller_test_case import get_project_manager_spec

from forty.controllers import controllers
from forty.managers import TimeManager

class TestFinishController(TestCase):
    def test_unique_keys(self):
        keys = set()

        pm = get_project_manager_spec()
        tm = TimeManager()

        for c in controllers:
            ci: controllers.AbstractController = c(pm=pm, tm=tm)
            for new_key in ci.keys:
                self.assertNotIn(new_key, keys)
                keys.add(new_key)
