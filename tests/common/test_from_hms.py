from unittest import TestCase

from forty.common import from_hms


class TestFromHMS(TestCase):
    def test_full_format(self):
        self.assertEqual(from_hms("12:34:56"), 45296)

    def test_full_format_and_leading_zero(self):
        self.assertEqual(from_hms("01:02:03"), 3723)

    def test_incorrect_value_without_seconds(self):
        with self.assertRaises(ValueError):
            from_hms("01:02:")

    def test_incorrect_value_without_seconds_and_colon(self):
        with self.assertRaises(ValueError):
            from_hms("01:02")

    def test_incorrect_value_without_minutes(self):
        with self.assertRaises(ValueError):
            from_hms("01:")

    def test_incorrect_value_without_minutes_and_colon(self):
        with self.assertRaises(ValueError):
            from_hms("01")

    def test_incorrect_value_empty(self):
        with self.assertRaises(ValueError):
            from_hms("")
