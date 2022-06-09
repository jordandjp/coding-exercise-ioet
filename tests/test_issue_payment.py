import unittest
from io import StringIO

from src.formatters import StringFormatter
from src.functions import issue_payment
from src.handlers import StreamHandler
from src.timeslot_parsers import SimpleTimeslotParser
from tests.fixtures import create_pay_table


class IssuePaymentTestCase(unittest.TestCase):
    def setUp(self):
        self.acme_table = create_pay_table()
        self.list_employee_raw_data = [
            "MARY=TU17:00-20:00",
            "JEFF=SU16:00-19:00,WE10:00-11:00,SA12:30-17:00",
            "ZACK=SU18:00-19:30,WE06:30-23:00,SA02:00-15:15",
        ]
        self.parser = SimpleTimeslotParser(
            timeslots_sep=",",
            name_sep="=",
            day_slice=slice(0, 2),
            times_sep="-",
            timeslot_format="%H:%M",
        )
        self.message_template = "The amount to pay {0.employee.name} is: {0.amount.value:0.0f} {0.amount.currency}"
        self.formatter = StringFormatter(self.message_template)
        self.handler = StreamHandler(StringIO())

    def test_issue_payment(self):
        list_expected = [
            "The amount to pay MARY is: 55 USD\n",
            "The amount to pay JEFF is: 170 USD\n",
            "The amount to pay ZACK is: 669 USD\n",
        ]
        for employee_raw_data, expected in zip(
            self.list_employee_raw_data, list_expected
        ):
            with self.subTest(employee_raw_data=employee_raw_data, expected=expected):
                issue_payment(
                    self.acme_table,
                    employee_raw_data,
                    self.parser,
                    self.formatter,
                    self.handler,
                )
                self.handler.file.seek(0)
                self.assertMultiLineEqual(self.handler.file.getvalue(), expected)
