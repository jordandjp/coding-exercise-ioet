import unittest

from src.load_table import load_csv_table
from src.model import PayTable
from tests.fixtures import create_pay_table


class LoadTableTestCase(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.acme_table = load_csv_table("tests/data/test_table_data.csv")

    def test_instance_load_csv_table(self):
        self.assertIsInstance(self.acme_table, PayTable)

    def test_load_csv_table(self):
        created_acme_table = create_pay_table()
        self.assertListEqual(
            self.acme_table.timeslots_pay_rate, created_acme_table.timeslots_pay_rate
        )
