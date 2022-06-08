import unittest

from src.model import Day, DayTimeslot, Employee, EmployeeTimeslots
from src.timeslot import Timeslot
from src.timeslot_parser import SimpleTimeslotParser


def create_employee_timeslots(name: str, days_timeslots: list):
    employee = Employee(name)
    days_timeslots = [
        DayTimeslot(day, Timeslot.strptime(start_time, end_time, format_time))
        for day, start_time, end_time, format_time in days_timeslots
    ]

    return EmployeeTimeslots(employee, days_timeslots)


class SimpleTimeslotParserTestCase(unittest.TestCase):
    def setUp(self):
        self.timeslot_parser = SimpleTimeslotParser(
            timeslots_sep=",",
            name_sep="=",
            day_slice=slice(0, 2),
            times_sep="-",
            timeslot_format="%H:%M",
        )
        self.timeslot_entry = (
            "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        )

        self.employee_timeslots_created = create_employee_timeslots(
            "RENE",
            [
                (Day.MONDAY, "10:00", "12:00", "%H:%M"),
                (Day.TUESDAY, "10:00", "12:00", "%H:%M"),
                (Day.THURSDAY, "01:00", "03:00", "%H:%M"),
                (Day.SATURDAY, "14:00", "18:00", "%H:%M"),
                (Day.SUNDAY, "20:00", "21:00", "%H:%M"),
            ],
        )
        self.employee_timeslots_parsed = self.timeslot_parser.parse(self.timeslot_entry)

    def test_parse_type_return(self):
        self.assertIsInstance(
            self.timeslot_parser.parse(self.timeslot_entry), EmployeeTimeslots
        )

    def test_parse_valid_string(self):

        self.assertListEqual(
            self.employee_timeslots_parsed.days_timeslot,
            self.employee_timeslots_created.days_timeslot,
        )

    def test_equal_len_employee_day_timeslots(self):
        self.assertEqual(
            len(self.employee_timeslots_parsed.days_timeslot),
            len(self.employee_timeslots_created.days_timeslot),
        )

    def test_same_employee(self):
        self.assertEqual(
            self.employee_timeslots_created.employee,
            self.employee_timeslots_parsed.employee,
        )
