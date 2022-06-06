import unittest

from src.daytime import DayTime


class DayTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.midnight = DayTime(0, 0)
        self.morning = DayTime(6, 0)

    def test_default_values(self):
        self.assertEqual(self.midnight.hour, 24)
        self.assertEqual(self.midnight.minute, 0)

    def test_midnight_greater_than_morning(self):
        self.assertGreater(self.midnight, self.morning)

    def test_morning_repr(self):
        self.assertEqual(repr(self.morning), "06:00")

    def test_24h(self):
        time_24h = DayTime(24, 0)
        self.assertEqual(time_24h, self.midnight)
        self.assertEqual(repr(time_24h), repr(self.midnight))

    def test_hour_validation(self):
        with self.assertRaises(ValueError):
            DayTime(24, 3)

    def test_minute_validation(self):
        with self.assertRaises(ValueError):
            DayTime(5, 60)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            DayTime(-5, -3)


if __name__ == "__main__":
    unittest.main()
