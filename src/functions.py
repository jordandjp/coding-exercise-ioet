from typing import List

from src.formatters import Formatter
from src.handlers import Handler
from src.model import PayTable
from src.timeslot_parser import TimeslotParser


def issue_payment(
    company_table: PayTable,
    employee_raw_data: List[str],
    parser: TimeslotParser,
    formatter: Formatter,
    handler: Handler,
) -> None:
    employee_timeslots = parser.parse(employee_raw_data)
    pay = company_table.calculate_employee_pay(employee_timeslots)
    message = formatter.format(pay)
    handler.emit(message)
