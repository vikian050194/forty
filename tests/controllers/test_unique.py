from unittest import skip
from unittest.case import TestCase

from .controller_test_case import get_file_manager_spec

import forty.controllers as controllers
from forty.managers import TimeManager


@skip("TODO reimplement test")
class TestController(TestCase):
    def test_unique_keys(self):
        keys = set()

        fm = get_file_manager_spec()
        tm = TimeManager()

        for c in controllers:
            ci: controllers.AbstractController = c(fm=fm, tm=tm)
            for new_key in ci.keys:
                self.assertNotIn(new_key, keys)
                keys.add(new_key)
