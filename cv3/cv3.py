import re
from typing import List


class RomanCalculator:

    def __init__(self):
        self.to_arabic_values = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
                                 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.to_roman_values = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                                2000: 'MM', 3000: 'MMM', 0: ''}
        self.numbers = []

    def convert_to_int(self, input_str: str) -> int:
        if not isinstance(input_str, str) or len(input_str) == 0:
            return -9999
        roman: str = input_str.upper()
        if self.wrong_format(roman):
            return -9999

        for key, value in self.to_arabic_values.items():
            roman = roman.replace(key, str(value) + ' ')

        self.numbers: List[int] = [int(x) for x in roman[:-1].split(' ')]

        result = sum(self.numbers)
        return self.check_result(result)

    def check_result(self, result: int) -> int:
        if len(self.numbers) > 1 and result in list(self.to_arabic_values.values()):
            return -9999
        sorted_numbers = sorted(self.numbers, reverse=True)
        if sorted_numbers == self.numbers:
            return result
        return -9999

    def wrong_format(self, input_str: str) -> False:
        for i in input_str:
            if i not in self.to_arabic_values.keys():
                return True

        incorrect_combinations = ['VV', 'LL', 'DD']
        incorrect_combinations.extend([x * 4 for x in list(self.to_arabic_values.keys())[6:]])
        incorrect_combinations.extend([x * 2 for x in list(self.to_arabic_values.keys())[:6]])

        for comb in incorrect_combinations:
            if comb in input_str:
                return True

        return False

    def convert_to_roman(self, to_convert: str) -> str:
        return ''.join([self.to_roman_values[int(to_convert[-i] + '0' * (i - 1))]
                        for i in range(1, len(to_convert) + 1)])[::-1]

    def calculate(self, expression: str) -> str:
        expression = expression.replace(' ', '')
        numbers = re.split(r'[-*/+]', expression)
        if len(numbers) != 2:
            return 'Zly vstup'
        num1 = self.convert_to_int(numbers[0])
        num2 = self.convert_to_int(numbers[1])
        if -9999 in [num1, num2]:
            return 'Zly vstup'
        result = int(eval(str(num1) + expression[len(numbers[0])] + str(num2)))
        if 1 <= result <= 3999:
            return self.convert_to_roman(str(result))
        return 'Cislo mimo'
