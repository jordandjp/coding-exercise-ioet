import itertools
import unittest

from src import model
from src.timeslot import Timeslot


def create_complete_pay_table():
    am = Timeslot.strptime("00:01", "12:00", "%H:%M")
    pm = Timeslot.strptime("12:01", "00:00", "%H:%M")

    money = itertools.cycle((model.Money(10), model.Money(20)))
    timeslots = []

    for day in model.Day:
        for period in (am, pm):
            day_timeslot = model.DayTimeslot(day, period)
            timeslots.append(model.TimeslotPayRate(day_timeslot, next(money)))

    return model.PayTable(timeslots)


class PayTableTestCase(unittest.TestCase):
    def setUp(self):
        self.pay_table = create_complete_pay_table()
        self.bob_employee = model.Employee("Bob")
        self.bob_employee_timeslots = model.EmployeeTimeslots(
            self.bob_employee,
            [
                model.DayTimeslot(
                    model.Day.MONDAY, Timeslot.strptime("06:00", "08:00", "%H:%M")
                ),
            ],
        )
        self.peter_employee = model.Employee("Peter")
        self.peter_employee_timeslots = model.EmployeeTimeslots(
            self.peter_employee,
            [
                model.DayTimeslot(
                    model.Day.TUESDAY, Timeslot.strptime("16:00", "18:00", "%H:%M")
                ),
                model.DayTimeslot(
                    model.Day.FRIDAY, Timeslot.strptime("10:00", "13:30", "%H:%M")
                ),
                model.DayTimeslot(
                    model.Day.SATURDAY, Timeslot.strptime("23:00", "00:00", "%H:%M")
                ),
            ],
        )

    def test_result_total_pay(self):
        self.assertIsInstance(
            self.pay_table.calculate_employee_pay(self.bob_employee_timeslots),
            model.Pay,
        )

    def test_empty_employee_timeslots(self):
        empty_employee_timeslots = model.EmployeeTimeslots(self.bob_employee, [])
        self.assertEqual(
            self.pay_table.calculate_employee_pay(empty_employee_timeslots),
            model.Pay(model.Money(0), self.bob_employee),
        )

    def test_calculate_single_timeslot_pay(self):
        self.assertEqual(
            self.pay_table.calculate_single_timeslot_pay(
                self.bob_employee_timeslots.days_timeslot[0], self.bob_employee
            ),
            model.Pay(model.Money(20), self.bob_employee),
        )

    def test_total_pay_multiple_timeslot(self):
        self.assertEqual(
            self.pay_table.calculate_employee_pay(self.peter_employee_timeslots),
            model.Pay(model.Money((20 * (4.5 - 1 / 60)) + 20), self.peter_employee),
        )
