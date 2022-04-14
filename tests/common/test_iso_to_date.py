from unittest import TestCase

from datetime import date

from forty.common import iso_to_date


call = iso_to_date


class TestIsoToDatet(TestCase):
    def test_today(self):
        expected = date(year=2022, month=3, day=10)
        actual = call("2022-03-10")
        self.assertEqual(actual, expected)
