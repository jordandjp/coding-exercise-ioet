import unittest

from src.formatters import StringFormatter
from src.model import Employee, Money, Pay


class StringFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.one_line_formatter = StringFormatter(
            "The amount to pay {0.employee.name} is: {0.amount.value} {0.amount.currency}",
        )
        self.multi_line_formatter = StringFormatter(
            "Payment:\n"
            "\tName: {0.employee.name}\n"
            "\tAmount: {0.amount.value}\n"
            "\tCurrency: {0.amount.currency}\n",
        )
        self.rene_pay = Pay(Money(35, "USD"), Employee("RENE"))
        self.bob_pay = Pay(Money(30, "GBP"), Employee("Bob"))

    def test_one_line_format(self):
        self.assertMultiLineEqual(
            self.one_line_formatter.format(self.rene_pay),
            "The amount to pay RENE is: 35 USD",
        )

    def test_multi_line_formatter(self):
        self.assertMultiLineEqual(
            self.multi_line_formatter.format(self.bob_pay),
            "Payment:\n\tName: Bob\n\tAmount: 30\n\tCurrency: GBP\n",
        )
