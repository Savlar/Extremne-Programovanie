import unittest
from data_parser import Parser


class DataTests(unittest.TestCase):

    def setUp(self) -> None:
        self.parser = Parser()

    def test_row_length(self):
        for row in self.parser.answers:
            self.assertTrue(self.parser.correct_row_length(row), 'Incorrect row length: ' + row)

    def test_question_number(self):
        i = 1
        for row in self.parser.answers:
            self.assertEqual(self.parser.question_order(row), i)
            i += 1

    def test_answer_is_digit(self):
        for row in self.parser.answers:
            for number in row.split(';'):
                self.assertTrue(self.parser.is_number(number), 'Wrong number: ' + repr(number))


if __name__ == '__main__':
    unittest.main()


# chyby
# - chybajuce cislo v dotazniku
# - mensi pocet odpovedi ako ma byt
# - nespravne cislo v odpovedi na otazku