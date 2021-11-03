from unittest import TestCase

from forty.common import int_to_hms


class TestIntToHMS(TestCase):
    def test_zero(self):
        self.assertEqual(int_to_hms(0), "00:00:00")

    def test_positive(self):
        self.assertEqual(int_to_hms(45296), "12:34:56")

    def test_negative(self):
        self.assertEqual(int_to_hms(-144000), "-40:00:00")
