from __future__ import annotations

from datetime import datetime

from src.daytime import DayTime


class Timeslot:
    """Abstraction that represent a time interval within a day.

    Not all time intervals are valid. Timeslot represents the intervals
    within the same day, and intervals that covers two days are not valid.
    Therefore, it is not possible for the end time to be less than the start time.
    """

    def __init__(self, start_time: DayTime, end_time: DayTime) -> None:
        if start_time > end_time:
            raise ValueError("End time must be greater that start time")

        self.start_time = start_time
        self.end_time = end_time

    def intersect_with(self, other: Timeslot) -> bool:
        """Check if two timeslots overlaps."""
        return self.__intersect_with(other)

    def intersection(self, other: Timeslot) -> Timeslot | int:
        """Returns a time range with overlapping times in both time ranges."""
        return self ^ other

    @property
    def total_hours(self):
        return (
            self.end_time.hour
            - self.start_time.hour
            + ((self.end_time.minute - self.start_time.minute) / 60)
        )

    @staticmethod
    def strptime(start_time: str, end_time: str, format_: str = "%H:%M") -> Timeslot:
        """A convenient and powerful way of creating Timeslot instances by
        taking advantage of the datetime.strptime method."""
        dt_start_time = datetime.strptime(start_time, format_)
        dt_end_time = datetime.strptime(end_time, format_)
        start_time = DayTime(
            hour=dt_start_time.hour,
            minute=dt_start_time.minute,
        )
        end_time = DayTime(
            hour=dt_end_time.hour,
            minute=dt_end_time.minute,
        )
        return Timeslot(start_time, end_time)

    def __intersect_with(self, other: Timeslot) -> bool:
        return (
            self.start_time <= other.start_time <= self.end_time
            or self.start_time <= other.end_time <= self.end_time
            or other.start_time <= self.start_time <= other.end_time
            or other.start_time <= self.end_time <= other.end_time
        )

    def __within(self, other: Timeslot) -> bool:
        """This timeslot is within the range of the other timeslot."""
        return (
            other.start_time <= self.start_time <= other.end_time
            and other.start_time <= self.end_time <= other.end_time
        )

    def __repr__(self) -> str:
        return f"{self.start_time!s}-{self.end_time!s}"

    def __eq__(self, other: Timeslot) -> str:
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __xor__(self, other: Timeslot) -> Timeslot | int:
        if not isinstance(other, Timeslot):
            raise TypeError(
                f"unsupported operand type(s) for ^: {other.__class__.__name__} and {self.__class__.__name__}"
            )
        if self.__within(other):
            result = self

        elif other.__within(self):
            result = other

        elif self.__intersect_with(other):
            if self.start_time <= other.start_time <= self.end_time:
                result = Timeslot(other.start_time, self.end_time)
            else:
                result = Timeslot(self.start_time, other.end_time)
        else:
            result = -1  # Sentinel value

        return result
