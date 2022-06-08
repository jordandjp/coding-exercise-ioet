import itertools
import unittest

from src.load_table import load_csv_table
from src.model import Day, DayTimeslot, Money, PayTable, TimeslotPayRate
from src.timeslot import Timeslot


def create_acme_pay_table():
    pay_rates = [25, 15, 20] * 5 + [30, 20, 25] * 2
    timeslots = [
        Timeslot.strptime("00:01", "09:00"),
        Timeslot.strptime("09:01", "18:00"),
        Timeslot.strptime("18:01", "00:00"),
    ] * 7
    days = itertools.chain.from_iterable(((itertools.repeat(day, 3)) for day in Day))
    pay_rate_timeslots = []

    for pay_rate, timeslot, day in zip(pay_rates, timeslots, days):
        day_timeslot = DayTimeslot(day, timeslot)
        pay_rate_timeslots.append(TimeslotPayRate(day_timeslot, Money(pay_rate)))

    return PayTable(pay_rate_timeslots)


class LoadTableTestCase(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.acme_table = load_csv_table("tests/data/test_table_data.csv")

    def test_instance_load_csv_table(self):
        self.assertIsInstance(self.acme_table, PayTable)

    def test_load_csv_table(self):
        created_acme_table = create_acme_pay_table()
        self.assertListEqual(
            self.acme_table.timeslots_pay_rate, created_acme_table.timeslots_pay_rate
        )
