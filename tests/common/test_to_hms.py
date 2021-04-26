from unittest import TestCase

from forty.common import to_hms


class TestToHMS(TestCase):
    def test_zero(self):
        self.assertEqual(to_hms(0), "00:00:00")

    def test_positive(self):
        self.assertEqual(to_hms(45296), "12:34:56")

    def test_negative(self):
        self.assertEqual(to_hms(-144000), "-40:00:00")
