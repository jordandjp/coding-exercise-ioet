"""Fixtures used by multiple test cases"""

import itertools

from src.model import Day, DayTimeslot, Money, PayTable, TimeslotPayRate
from src.timeslot import Timeslot


def create_pay_table():
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
