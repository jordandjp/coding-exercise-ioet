import unittest


from src.readers import read_txt_employee_data


class ReadTxtEmployeeDataTestCase(unittest.TestCase):
    def setUp(self):
        self.raw_data = read_txt_employee_data("tests/data/test_input_data.txt")

    def test_len_elements_equal_num_lines(self):
        self.assertEqual(len(self.raw_data), 5)

    def test_first_line(self):
        self.assertEqual(
            self.raw_data[0],
            "TOM=TH15:00-22:00,TU01:00-20:15,SU16:30-23:45,WE09:30-21:30",
        )

    def test_not_new_line(self):
        for line in self.raw_data:
            with self.subTest(line=line):
                self.assertFalse("\n" in line)
