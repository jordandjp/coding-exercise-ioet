import csv
from os import PathLike
from typing import Union

from src.model import Day, DayTimeslot, Money, PayTable, TimeslotPayRate
from src.timeslot import Timeslot


def load_csv_table(file: Union[str, bytes, PathLike]) -> PayTable:
    """Read a comma-separated values (csv) file into PayTable"""

    day_map = {
        "MO": Day.MONDAY,
        "TU": Day.TUESDAY,
        "WE": Day.WEDNESDAY,
        "TH": Day.THURSDAY,
        "FR": Day.FRIDAY,
        "SA": Day.SATURDAY,
        "SU": Day.SUNDAY,
    }

    with open(file, mode="rt", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        pay_rate_timeslots = []

        for row in reader:
            timeslot = Timeslot.strptime(row["start_time"], row["end_time"])
            day_timeslot = DayTimeslot(day_map[row["day"]], timeslot)
            pay_rate_timeslots.append(
                TimeslotPayRate(
                    day_timeslot, Money(int(row["hourly_rate"]), row["currency"])
                )
            )

        return PayTable(pay_rate_timeslots)
