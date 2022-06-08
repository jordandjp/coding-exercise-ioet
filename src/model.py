from __future__ import annotations

import calendar
from dataclasses import dataclass
from enum import Enum
from typing import List

from src.timeslot import Timeslot


class Day(Enum):
    MONDAY = calendar.MONDAY
    TUESDAY = calendar.TUESDAY
    WEDNESDAY = calendar.WEDNESDAY
    THURSDAY = calendar.THURSDAY
    FRIDAY = calendar.FRIDAY
    SATURDAY = calendar.SATURDAY
    SUNDAY = calendar.SUNDAY


@dataclass(frozen=True)
class Money:
    value: int
    currency: str = "USD"

    def __add__(self, other: Money) -> Money:
        if self.currency != other.currency:
            ValueError("Money objects must be of the same currency")

        return Money(self.value + other.value, self.currency)

    def __mul__(self, other: int) -> Money:
        return Money(self.value * other, self.currency)

    def __rmul__(self, other: int) -> Money:
        return self * other


@dataclass(frozen=True)
class DayTimeslot:
    day: Day
    timeslot: Timeslot

    def intersect_with(self, other: DayTimeslot) -> bool:
        return self.day == other.day and self.timeslot.intersect_with(other.timeslot)

    def intersection(self, other: DayTimeslot) -> DayTimeslot | int:
        result = -1
        if self.intersect_with(other):
            result = DayTimeslot(self.day, self.timeslot ^ other.timeslot)
        return result


@dataclass(frozen=True)
class TimeslotPayRate:
    day_timeslot: DayTimeslot
    hourly_rate: Money


@dataclass(frozen=True)
class TimeslotPayRate:
    day_timeslot: DayTimeslot
    pay_rate: Money


@dataclass(frozen=True)
class Employee:
    name: str


@dataclass(frozen=True)
class EmployeeTimeslots:
    employee: Employee
    days_timeslot: List[DayTimeslot]


@dataclass(frozen=True)
class Pay:
    amount: Money
    employee: Employee


class PayTable:
    """An abstraction that represents the information of the payment rate
    per time interval of the days of the week."""

    def __init__(
        self, timeslots_pay_rate: List[TimeslotPayRate], currency: str = "USD"
    ) -> None:
        self.timeslots_pay_rate = timeslots_pay_rate
        self.currency = currency

    def calculate_employee_pay(self, employee_timeslots: EmployeeTimeslots) -> Pay:
        """Calculate the total amount to be paid for the employee's hours worked"""
        money = Money(0, self.currency)

        for employee_day_timeslot in employee_timeslots.days_timeslot:
            single_pay = self.calculate_single_timeslot_pay(
                employee_day_timeslot, employee_timeslots.employee
            )
            money = money + single_pay.amount

        return Pay(money, employee_timeslots.employee)

    def calculate_single_timeslot_pay(
        self, day_timeslot: DayTimeslot, employee: Employee
    ) -> Pay:
        money = Money(0, self.currency)

        for timeslot_pay_rate in self.timeslots_pay_rate:
            if day_timeslot.intersect_with(timeslot_pay_rate.day_timeslot):
                dts = day_timeslot.intersection(timeslot_pay_rate.day_timeslot)
                money = money + (dts.timeslot.total_hours * timeslot_pay_rate.pay_rate)

        return Pay(money, employee)
