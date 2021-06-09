from unittest import TestCase, skip

from forty.common import to_int


call = to_int


class TestToInt(TestCase):
    def test_full_format(self):
        expected = 45296
        actual = call("12:34:56")
        self.assertEqual(actual, expected)

    def test_full_format_with_leading_zero(self):
        expected = 3723
        actual = call("01:02:03")
        self.assertEqual(actual, expected)

    def test_hours(self):
        expected = 10800
        actual = call("3")
        self.assertEqual(actual, expected)

    def test_hours_with_leadind_zero(self):
        expected = 10800
        actual = call("03")
        self.assertEqual(actual, expected)

    def test_hours_with_colon(self):
        expected = 10800
        actual = call("03:")
        self.assertEqual(actual, expected)

    def test_hours_with_two_colons(self):
        expected = 10800
        actual = call("03::")
        self.assertEqual(actual, expected)

    def test_minutes(self):
        expected = 180
        actual = call(":3:")
        self.assertEqual(actual, expected)

    def test_minutes_with_leadind_zero(self):
        expected = 180
        actual = call(":03:")
        self.assertEqual(actual, expected)

    def test_seconds(self):
        expected = 3
        actual = call("::3")
        self.assertEqual(actual, expected)

    def test_seconds_with_leadind_zero(self):
        expected = 3
        actual = call("::03")
        self.assertEqual(actual, expected)

    def test_hours_and_minutes(self):
        expected = 10800 + 120
        actual = call("3:2")
        self.assertEqual(actual, expected)

    def test_hours_and_minutes_with_leadind_zero(self):
        expected = 10800 + 120
        actual = call("03:02")
        self.assertEqual(actual, expected)

    def test_hours_and_minutes_with_three_colons(self):
        expected = 10800 + 120
        actual = call("03:02:")
        self.assertEqual(actual, expected)

    def test_minutes_and_seconds(self):
        expected = 120 + 1
        actual = call(":2:1")
        self.assertEqual(actual, expected)

    def test_minutes_and_seconds_with_leadind_zero(self):
        expected = 120 + 1
        actual = call(":02:01")
        self.assertEqual(actual, expected)

    def test_incorrect_value_empty(self):
        with self.assertRaises(ValueError):
            call("")
