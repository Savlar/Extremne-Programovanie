class Parser:

    def __init__(self):
        self.file_name = 'suborDat.txt'
        self.file_rows = self.parse_file()
        self.answers = self.file_rows[1:]
        self.row_length = len(self.file_rows[0].split(';'))

    def parse_file(self):
        with open(self.file_name, 'r', encoding='UTF-8-SIG') as file:
            rows = file.read().split('\n')[:-1]
        return rows

    def correct_row_length(self, row: str) -> bool:
        return len(row.split(';')) == self.row_length

    @staticmethod
    def question_order(row):
        return int(row.split(';')[0])

    @staticmethod
    def is_number(number):
        try:
            int(number)
            return True
        except ValueError:
            return False
