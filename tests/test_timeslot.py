import unittest

from src.daytime import DayTime
from src.timeslot import Timeslot


class TimeslotTestCase(unittest.TestCase):
    def setUp(self):
        self.morning = Timeslot(DayTime(6, 0), DayTime(12, 0))
        self.afternoon = Timeslot(DayTime(12, 1), DayTime(18, 0))
        self.employee_timeslot = Timeslot(DayTime(14, 0), DayTime(16, 0))

    def test_employee_timeslot_intersect_with(self):
        self.assertTrue(self.employee_timeslot.intersect_with(self.afternoon))
        self.assertFalse(self.employee_timeslot.intersect_with(self.morning))

    def test_employee_timeslot_repr(self):
        self.assertEqual(repr(self.employee_timeslot), "14:00-16:00")

    def test_employee_intersection_afternoon(self):
        self.assertEqual(
            self.employee_timeslot.intersection(self.afternoon), self.employee_timeslot
        )

    def test_afternoon_intersection_morning(self):
        self.assertEqual(self.afternoon.intersection(self.morning), -1)

    def test_employees_intersection(self):
        employee2_timeslot = Timeslot(DayTime(13, 30), DayTime(15, 15))
        self.assertEqual(
            employee2_timeslot.intersection(self.employee_timeslot),
            Timeslot(DayTime(14, 0), DayTime(15, 15)),
        )

    def test_timeslot_strptime(self):
        timeslot = Timeslot.strptime("18:00", "22:00", "%H:%M")
        self.assertEqual(timeslot, Timeslot(DayTime(18, 0), DayTime(22, 0)))


if __name__ == "__main__":
    unittest.main()
