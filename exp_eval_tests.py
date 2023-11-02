# Start of unittest - add to completely test functions in exp_eval
#changes made
import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("2 2 ** 2 >> "), 1)

    def test_postfix_eval_(self):
        self.assertAlmostEqual(postfix_eval("12"), 12.0)
    def test_postfix_eval_0(self):
        self.assertEqual(postfix_eval("2 2 ** 2 << "), 16)
    def test_postfix_eval_00(self):
        self.assertEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3  5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    def test_postfix_eval_05(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 0 /")
    def test_postfix_eval_06(self):
        try:
            postfix_eval('3 5 / -10 >>')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')
    def test_postfix_eval_08(self):
        try:
            postfix_eval('3 5 / -10 <<')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_postfix_eval_07(self):
        try:
            postfix_eval('                     ')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Empty input')

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("2 * (  5 -   3  ) + 7 * ( 4 ** 9 ) - 58"), "2 5 3 - * 7 4 9 ** * + 58 -")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix("5  * ( 34 ** 6 ) * ( 8 - 6 + 2 )"), "5 34 6 ** * 8 6 - 2 + *")

    def test_prefix_to_postfix1(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix2(self):
        self.assertEqual(prefix_to_postfix("* * 5 ** 34 6 + - 8 6 2"), "5 34 6 ** * 8 6 - 2 + *")

    def test_prefix_to_postfix3(self):
        self.assertEqual(prefix_to_postfix("<< 2 2"), "2 2 <<")

    def test_prefix_to_postfix4(self):
        self.assertEqual(prefix_to_postfix(">> 2 2"), "2 2 >>")

if __name__ == "__main__":
    unittest.main()
