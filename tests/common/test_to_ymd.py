from unittest import TestCase

from datetime import datetime

from forty.common import to_ymd


class TestToYMD(TestCase):
    def test_today(self):
        self.assertEqual(to_ymd(datetime(year=2021, month=4, day=11)), "2021-04-11")
