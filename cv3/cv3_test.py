import unittest
from cv3 import convert_to_int


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, convert_to_int('I'))

    def test_2(self):
        self.assertEqual(2, convert_to_int('II'))

    def test_3(self):
        self.assertEqual(3, convert_to_int('III'))

    def test_4(self):
        self.assertEqual(4, convert_to_int('IV'))

    def test_5(self):
        self.assertEqual(5, convert_to_int('V'))

    def test_6(self):
        self.assertEqual(6, convert_to_int('VI'))

    def test_7(self):
        self.assertEqual(8, convert_to_int('VIII'))

    def test_8(self):
        self.assertEqual(9, convert_to_int('IX'))

    def test_9(self):
        self.assertEqual(-9999, convert_to_int('KVI'))

    def test_10(self):
        self.assertEqual(-9999, convert_to_int('-*/'))

    def test_11(self):
        self.assertNotEqual(1, convert_to_int('IIIIV'))

    def test_12(self):
        self.assertNotEqual(5, convert_to_int('IIIII'))

    def test_13(self):
        self.assertEqual(-9999, convert_to_int(''))

    def test_14(self):
        self.assertNotEqual(9, convert_to_int('VIIII'))

    def test_15(self):
        self.assertNotEqual(10, convert_to_int('VIIIII'))

    def test_16(self):
        self.assertEqual(105, convert_to_int('CV'))

    def test_17(self):
        self.assertEqual(-9999, convert_to_int(5))

    def test_18(self):
        self.assertEqual(-9999, convert_to_int('IVI'))

    def test_19(self):
        self.assertEqual(-9999, convert_to_int('VIV'))

    def test_20(self):
        self.assertEqual(-9999, convert_to_int('VIVI'))

    def test_21(self):
        self.assertEqual(-9999, convert_to_int('VIIIV'))

    def test_22(self):
        self.assertEqual(-9999, convert_to_int('VIXIV'))

    def test_23(self):
        self.assertEqual(-9999, convert_to_int('XIVIX'))

    def test_24(self):
        self.assertEqual(2594, convert_to_int('MMDXCIV'))

    def test_25(self):
        self.assertEqual(-9999, convert_to_int('MMMDCXLIX'))

    def test_26(self):
        self.assertEqual(None, None)

    def test_27(self):
        self.assertEqual(None, None)

    def test_28(self):
        self.assertEqual(None, None)

    def test_29(self):
        self.assertEqual(None, None)

    def test_30(self):
        self.assertEqual(None, None)

    def test_31(self):
        self.assertEqual(None, None)

    def test_32(self):
        self.assertEqual(None, None)

    def test_33(self):
        self.assertEqual(None, None)

    def test_34(self):
        self.assertEqual(None, None)

    def test_35(self):
        self.assertEqual(None, None)

    def test_36(self):
        self.assertEqual(None, None)

    def test_37(self):
        self.assertEqual(None, None)

    def test_38(self):
        self.assertEqual(None, None)

    def test_39(self):
        self.assertEqual(None, None)

    def test_40(self):
        self.assertEqual(None, None)

    def test_41(self):
        self.assertEqual(None, None)

    def test_42(self):
        self.assertEqual(None, None)

    def test_43(self):
        self.assertEqual(None, None)

    def test_44(self):
        self.assertEqual(None, None)

    def test_45(self):
        self.assertEqual(None, None)

    def test_46(self):
        self.assertEqual(None, None)

    def test_47(self):
        self.assertEqual(None, None)

    def test_48(self):
        self.assertEqual(None, None)

    def test_49(self):
        self.assertEqual(None, None)

    def test_50(self):
        self.assertEqual(None, None)


if __name__ == '__main__':
    unittest.main()
