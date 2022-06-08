import unittest

from src.formatters import StringFormatter
from src.model import Employee, Money, Pay


class StringFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.one_line_formatter = StringFormatter(
            "The amount to pay {obj.employee.name} is: {obj.amount.value} {obj.amount.currency}",
            "obj",
        )
        self.multi_line_formatter = StringFormatter(
            "Payment:\n"
            "\tName: {pay.employee.name}\n"
            "\tAmount: {pay.amount.value}\n"
            "\tCurrency: {pay.amount.currency}\n",
            "pay",
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


if __name__ == "__main__":
    unittest.main()
