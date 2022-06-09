import argparse
import sys

from src.formatters import StringFormatter
from src.functions import issue_payment
from src.handlers import StreamHandler
from src.load_table import load_csv_table
from src.readers import read_txt_employee_data
from src.timeslot_parsers import SimpleTimeslotParser


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate the total that company has to pay to employees, "
        "based on the hours they worked and the times during which they worked."
    )

    parser.add_argument(
        "-e",
        "--employee-schedule",
        help="txt file containing the employee schedule",
        type=str,
        default="data/input_data.txt",
    )
    parser.add_argument(
        "-c",
        "--company-table",
        help="csv file containing the company table pay rates",
        type=str,
        default="data/ACME_TABLE.csv",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    company_table = load_csv_table(args.company_table)
    raw_employees_schedule = read_txt_employee_data(args.employee_schedule)

    parser = SimpleTimeslotParser(
        timeslots_sep=",",
        name_sep="=",
        day_slice=slice(0, 2),
        times_sep="-",
        timeslot_format="%H:%M",
    )
    message_template = "The amount to pay {0.employee.name} is: {0.amount.value:0.0f} {0.amount.currency}"
    formatter = StringFormatter(message_template)
    handler = StreamHandler(sys.stdout)
    for raw_single_data in raw_employees_schedule:
        issue_payment(company_table, raw_single_data, parser, formatter, handler)


if __name__ == "__main__":
    main()
