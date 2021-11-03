from unittest import TestCase

from datetime import datetime

from forty.common import dt_to_ymd


class TestDtToYMD(TestCase):
    def test_today(self):
        self.assertEqual(dt_to_ymd(datetime(year=2021, month=4, day=11)), "2021-04-11")
