from dataclasses import dataclass


@dataclass(order=True)
class DayTime:
    """Abstraction that represents a time of the day in terms of hour and minute.

    00:01 is considered the first minute of the day and 00:00 the last one. Therefore
    00:00 < 00:01 is false."""

    hour: int
    minute: int

    def __repr__(self) -> str:
        return f"{self.hour % 24:0>2d}:{self.minute:0>2d}"

    def __post_init__(self) -> None:

        if self.hour > 24 or self.hour < 0:
            raise ValueError("hour must be in 0..24")

        if self.hour == 24 and self.minute > 0:
            raise ValueError("when hour is 24, minute must be 0")

        if self.minute > 59 or self.minute < 0:
            raise ValueError("minute must be in 0..59")

        # 00:00 is considered the last minute of the day
        if self.hour == 0 and self.minute == 0:
            self.hour = 24
