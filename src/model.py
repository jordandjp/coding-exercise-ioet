from __future__ import annotations

import calendar
from dataclasses import dataclass
from enum import Enum
from typing import List

from src.timeslot import Timeslot


class Day(Enum):
    MONDAY = calendar.MONDAY
    THURSDAY = calendar.THURSDAY
    WEDNESDAY = calendar.WEDNESDAY
    TUESDAY = calendar.TUESDAY
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

    def calculate_employee_pay(self, employee_timeslots: EmployeeTimeslots) -> Pay:
        """Calculate the total amount to be paid for the employee's hours worked"""
