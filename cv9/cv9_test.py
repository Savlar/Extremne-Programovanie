import unittest
from cv9 import RomanCalculator


class MyTestCase(unittest.TestCase):

    INPUT_IS_WRONG = -9999

    def setUp(self) -> None:
        self.c = RomanCalculator()

    def test_1(self):
        self.assertEqual(1, self.c.convert_to_int('I'))

    def test_2(self):
        self.assertEqual(2, self.c.convert_to_int('II'))

    def test_3(self):
        self.assertEqual(3, self.c.convert_to_int('III'))

    def test_4(self):
        self.assertEqual(4, self.c.convert_to_int('IV'))

    def test_5(self):
        self.assertEqual(5, self.c.convert_to_int('V'))

    def test_6(self):
        self.assertEqual(6, self.c.convert_to_int('VI'))

    def test_7(self):
        self.assertEqual(8, self.c.convert_to_int('VIII'))

    def test_8(self):
        self.assertEqual(9, self.c.convert_to_int('IX'))

    def test_9(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('KVI'))

    def test_10(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('-*/'))

    def test_11(self):
        self.assertNotEqual(1, self.c.convert_to_int('IIIIV'))

    def test_12(self):
        self.assertNotEqual(5, self.c.convert_to_int('IIIII'))

    def test_13(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int(''))

    def test_14(self):
        self.assertNotEqual(9, self.c.convert_to_int('VIIII'))

    def test_15(self):
        self.assertNotEqual(10, self.c.convert_to_int('VIIIII'))

    def test_16(self):
        self.assertEqual(105, self.c.convert_to_int('CV'))

    def test_17(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int(5))

    def test_18(self):
        self.assertEqual(1351, self.c.convert_to_int('MCCCLI'))

    def test_19(self):
        self.assertEqual(1323, self.c.convert_to_int('MCCCXXIII'))

    def test_20(self):
        self.assertEqual(3988, self.c.convert_to_int('MMMCMLXXXVIII'))

    def test_21(self):
        self.assertEqual(2788, self.c.convert_to_int('MMDCCLXXXVIII'))

    def test_22(self):
        self.assertEqual(2798, self.c.convert_to_int('MMDCCXCVIII'))

    def test_23(self):
        self.assertEqual(3178, self.c.convert_to_int('MMMCLXXVIII'))

    def test_24(self):
        self.assertEqual(2594, self.c.convert_to_int('MMDXCIV'))

    def test_25(self):
        self.assertEqual(3649, self.c.convert_to_int('MMMDCXLIX'))

    def test_26(self):
        self.assertEqual(3, self.c.convert_to_int('iii'))

    def test_27(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('IXX'))

    def test_28(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('IVIVIV'))

    def test_29(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('IIX'))

    def test_30(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('IXIXIX'))

    def test_31(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('XCX'))

    def test_32(self):
        self.assertEqual(89, self.c.convert_to_int('LXXXIX'))

    def test_33(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int(''))

    def test_34(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('     '))

    def test_35(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('MCMM'))

    def test_36(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('XCD'))

    def test_37(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('XXMM'))

    def test_38(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('MCCCMI'))

    def test_39(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('LC'))

    def test_40(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('DM'))

    def test_41(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('VL'))

    def test_42(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('IVI'))

    def test_43(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('LXL'))

    def test_44(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('XCX'))

    def test_45(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('IIV'))

    def test_46(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int('VIV'))

    def test_47(self):
        self.assertEqual('XX', self.c.calculate(' XI   + I X '))

    def test_48(self):
        self.assertEqual('Zly vstup', self.c.calculate(' MD '))

    def test_49(self):
        self.assertEqual('V', self.c.calculate('XXV/V'))

    def test_50(self):
        self.assertEqual('MCCXXII', self.c.calculate('MMCDXLIV-MCCXXII'))

    def test_51(self):
        self.assertEqual('Zly vstup', self.c.calculate(' MMMM + I'))

    def test_52(self):
        self.assertEqual('Zly vstup', self.c.calculate('MM @ I'))

    def test_53(self):
        self.assertEqual('Cislo mimo', self.c.calculate('MCDXLIV / MCDXLV'))

    def test_54(self):
        self.assertEqual('Cislo mimo', self.c.calculate('MMM + M'))

    def test_55(self):
        for i in range(1, 4000):
            roman: str = self.c.convert_to_roman(str(i))
            self.assertEqual(i, self.c.convert_to_int(roman), "Wrong convert from arabic to roman")

    def test_56(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int_with_alphabet('', 'IV'))

    def test_57(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int_with_alphabet('I', 'IV'))

    def test_58(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int_with_alphabet('IL', 'IV'))

    def test_59(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int_with_alphabet('IVXLX', 'IV'))

    def test_60(self):
        self.assertEqual(self.INPUT_IS_WRONG, self.c.convert_to_int_with_alphabet('IVI', 'IV'))

    def test_61(self):
        self.assertEqual(1351, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MCCCLI'))

    def test_62(self):
        self.assertEqual(1323, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MCCCXXIII'))

    def test_63(self):
        self.assertEqual(3988, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MMMCMLXXXVIII'))

    def test_64(self):
        self.assertEqual(2788, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MMDCCLXXXVIII'))

    def test_65(self):
        self.assertEqual(2798, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MMDCCXCVIII'))

    def test_66(self):
        self.assertEqual(3178, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MMMCLXXVIII'))

    def test_67(self):
        self.assertEqual(2594, self.c.convert_to_int_with_alphabet('IVXLCDM', 'MMDXCIV'))

    def test_68(self):
        self.assertEqual(3, self.c.convert_to_int_with_alphabet('A', 'AAA'))

    def test_69(self):
        self.assertEqual(1015, self.c.convert_to_int_with_alphabet('IAVXLCQDM', 'QVA'))

    def test_70(self):
        self.assertEqual(300000, self.c.convert_to_int_with_alphabet('IVXLCDMPQRS', 'SSS'))



if __name__ == '__main__':
    unittest.main()
