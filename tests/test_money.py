import unittest

from src.model import Money


class MoneyTestCase(unittest.TestCase):
    def setUp(self):
        self.fiver = Money(5, "USD")
        self.tenner = Money(10, "USD")

    def test_can_add_money_same_currency(self):
        self.assertEqual(self.fiver + self.fiver, self.tenner)

    def test_can_multiply_money_by_a_number(self):
        self.assertEqual(self.fiver * 20, Money(100))

    def test_can_multiply_a_number_by_money(self):
        self.assertEqual(2 * self.fiver, self.tenner)


if __name__ == "__main__":
    unittest.main()
