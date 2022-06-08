import unittest

from src.timeslot import Timeslot
from src.model import Day, DayTimeslot


class DayTimeslotTestCase(unittest.TestCase):
    def setUp(self):
        self.monday_morning_day_timeslot = DayTimeslot(
            Day.MONDAY, Timeslot.strptime("6:00", "12:00")
        )
        self.friday_afternoon_day_timeslot = DayTimeslot(
            Day.FRIDAY, Timeslot.strptime("12:01", "18:00")
        )
        self.friday_employee_day_timeslot = DayTimeslot(
            Day.FRIDAY, Timeslot.strptime("11:00", "16:00")
        )

    def test_same_day_intersect_with(self):
        self.assertTrue(
            self.friday_employee_day_timeslot.intersect_with(
                self.friday_afternoon_day_timeslot
            )
        )

    def test_different_days_intersect_with(self):
        sunday_morning = DayTimeslot(Day.SUNDAY, Timeslot.strptime("6:00", "12:00"))
        self.assertFalse(
            self.monday_morning_day_timeslot.intersect_with(sunday_morning)
        )

    def test_same_day_intersection(self):
        self.assertEqual(
            self.friday_employee_day_timeslot.intersection(
                self.friday_afternoon_day_timeslot
            ),
            DayTimeslot(Day.FRIDAY, Timeslot.strptime("12:00", "16:00")),
        )

    def test_different_days_intersection(self):
        sunday_morning = DayTimeslot(Day.SUNDAY, Timeslot.strptime("6:00", "12:00"))
        self.assertEqual(
            self.monday_morning_day_timeslot.intersection(sunday_morning), -1
        )


if __name__ == "__main__":
    unittest.main()
