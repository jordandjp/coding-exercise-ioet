import abc

from src.model import Day, DayTimeslot, Employee, EmployeeTimeslots
from src.timeslot import Timeslot


class TimeslotParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, string: str) -> EmployeeTimeslots:
        ...


class SimpleTimeslotParser(TimeslotParser):
    """
    spec        ::=       [name][[name_sep][day][start_time][times_sep][end_time][timeslots_sep]]

    name: <Any string>
    start_time, end_time: <Any string> that can be parsed by datetime.strptime
    day: <Any string> that represent a day of the week

    # Instance attributes
    name_sep: <Any token> that separates the name with the timeslots
    times_sep: <Any token> that separates the time start and the end time of the timeslots
    timeslots_sep: <Any token> that separates the timeslots

    day_slice: <Slice> that represents the start and final position of the day
    timeslot_format: <format> using the respective directives for hour and minute

    """

    day_map = {
        "MO": Day.MONDAY,
        "TU": Day.TUESDAY,
        "WE": Day.WEDNESDAY,
        "TH": Day.THURSDAY,
        "FR": Day.FRIDAY,
        "SA": Day.SATURDAY,
        "SU": Day.SUNDAY,
    }

    def __init__(
        self,
        timeslots_sep: str,
        name_sep: str,
        day_slice: slice,
        times_sep: str,
        timeslot_format: str = "%H:%M",
    ) -> None:
        self.timeslots_sep = timeslots_sep
        self.name_sep = name_sep
        self.day_slice = day_slice
        self.times_sep = times_sep
        self.timeslot_format = timeslot_format

    def parse(self, string: str) -> EmployeeTimeslots:

        name, string = string.split(self.name_sep)
        days_timeslot = string.split(self.timeslots_sep)

        return EmployeeTimeslots(
            Employee(name), [self.parse_day_timeslot(ts) for ts in days_timeslot]
        )

    def parse_day_timeslot(self, string: str) -> DayTimeslot:

        day = SimpleTimeslotParser.day_map[string[self.day_slice]]
        timeslot_string = string[self.day_slice.stop :]
        start_time, end_time = timeslot_string.split(self.times_sep)

        return DayTimeslot(
            day, Timeslot.strptime(start_time, end_time, self.timeslot_format)
        )
