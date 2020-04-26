import math
import re
from typing import List


class RomanCalculator:
    INPUT_IS_WRONG = -9999

    def __init__(self):
        self.to_arabic_values = {}
        self.to_roman_values = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                                2000: 'MM', 3000: 'MMM', 0: ''}
        self.numbers = []

    def convert_to_int(self, input_str: str, set_default_alphabet=True) -> int:
        if set_default_alphabet:
            self._setAlphabet(list('IVXLCDM'))
        if not isinstance(input_str, str) or len(input_str) == 0:
            return self.INPUT_IS_WRONG
        roman: str = input_str.upper()
        if self.wrong_format(roman):
            return self.INPUT_IS_WRONG

        for key in sorted(self.to_arabic_values.keys(), key=len, reverse=True):
            roman = roman.replace(key, str(self.to_arabic_values[key]) + ' ')

        self.numbers: List[int] = [int(x) for x in roman[:-1].split(' ')]

        result = sum(self.numbers)
        return self.check_result(result)

    def convert_to_int_with_alphabet(self, letters: str, input_str: str) -> int:
        alphabet = self._getAlphabet(letters)
        if len(alphabet) == 0:
            return self.INPUT_IS_WRONG
        used_letters = set(input_str)
        if used_letters & set(alphabet) != used_letters:
            return self.INPUT_IS_WRONG
        self._setAlphabet(alphabet)
        return self.convert_to_int(input_str, False)

    def max_number(self, roman_letters) -> int:
        if len(roman_letters) == 0 or len(roman_letters) != len(set(roman_letters)) \
                or roman_letters != roman_letters.upper():
            return self.INPUT_IS_WRONG
        length = len(roman_letters)
        if length == 1:
            return 3
        elif length == 2:
            return 8
        if length % 2 == 0:
            exp = (length // 2) - 1
            return self.dec(exp) + 5 * (10 ** math.floor(length / 2 - 1))
        exp = (length // 2)
        return self.dec(exp)

    @staticmethod
    def dec(exp: int) -> int:
        return 3 * (10 ** exp) + (10 ** exp) - 1

    def _setAlphabet(self, alphabet: list) -> None:
        self.to_arabic_values.clear()
        notRemain = len(alphabet) % 3 != 0
        for i in range(len(alphabet) // 2 + int(notRemain)):
            try:
                coefficient = 10 ** i
                self.to_arabic_values[alphabet[i * 2]] = 1 * coefficient
                self.to_arabic_values[alphabet[i * 2] + alphabet[i * 2 + 1]] = 4 * coefficient
                self.to_arabic_values[alphabet[i * 2 + 1]] = 5 * coefficient
                self.to_arabic_values[alphabet[i * 2] + alphabet[i * 2 + 2]] = 9 * coefficient
                self.to_arabic_values[alphabet[i * 2 + 2]] = 10 * coefficient
            except IndexError:
                pass

    @staticmethod
    def _getAlphabet(letters: str) -> list:
        en_alphabet = list(map(chr, range(ord('A'), ord('Z') + 1)))
        final_alphabet = []
        for letter in letters:
            if letter not in en_alphabet or letter in final_alphabet:
                final_alphabet.clear()
                break
            final_alphabet.append(letter)
        return final_alphabet

    def check_result(self, result: int) -> int:
        if len(self.numbers) > 1 and result in list(self.to_arabic_values.values()):
            return self.INPUT_IS_WRONG
        sorted_numbers = sorted(self.numbers, reverse=True)
        if sorted_numbers == self.numbers:
            return result
        return self.INPUT_IS_WRONG

    def wrong_format(self, input_str: str) -> False:
        for i in input_str:
            if i not in self.to_arabic_values.keys():
                return True

        incorrect_combinations = [x * 2 for x in list(self.to_arabic_values.keys())
                                  if '5' in str(self.to_arabic_values[x])]
        incorrect_combinations.extend([x * 4 for x in list(self.to_arabic_values.keys())
                                       if len(x) == 1])
        incorrect_combinations.extend([x * 2 for x in list(self.to_arabic_values.keys())
                                       if len(x) > 1])

        for comb in incorrect_combinations:
            if comb in input_str:
                return True

        return False

    def convert_to_roman(self, to_convert: str) -> str:
        return ''.join([self.to_roman_values[int(to_convert[-i] + '0' * (i - 1))]
                        for i in reversed(range(1, len(to_convert) + 1))])

    def calculate(self, expression: str) -> str:
        expression = expression.replace(' ', '')
        numbers = re.split(r'[-*/+]', expression)
        if len(numbers) != 2:
            return 'Zly vstup'
        num1 = self.convert_to_int(numbers[0])
        num2 = self.convert_to_int(numbers[1])
        if self.INPUT_IS_WRONG in [num1, num2]:
            return 'Zly vstup'
        result = int(eval(str(num1) + expression[len(numbers[0])] + str(num2)))
        if 1 <= result <= 3999:
            return self.convert_to_roman(str(result))
        return 'Cislo mimo'
