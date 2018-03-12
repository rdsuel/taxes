import unittest
import sys
from .tax_bracket import Bracket, BracketElement

# 2018 Married Filing Joint Bracket
bracket = Bracket(
    '2018 Married Filing Jointly',
    [
        BracketElement('10%', 0, 19050, 0.10),
        BracketElement('12%', 19051, 77400, 0.12),
        BracketElement('22%', 77401, 165000, 0.22),
        BracketElement('24%', 165001, 315000, 0.24),
        BracketElement('32%', 315001, 400000, 0.32),
        BracketElement('35%', 400001, 600000, 0.35),
        BracketElement('37%', 600001, sys.maxsize, 0.37),
    ])


class MyTestCase(unittest.TestCase):
    def test_tax_bracket_0(self):
        self.assertEqual(0, bracket.calculate_tax(0))

    def test_tax_bracket_10(self):
        self.assertEqual(1905, bracket.calculate_tax(19050))

    def test_tax_bracket_12(self):
        self.assertEqual(8907, bracket.calculate_tax(77400))

    def test_tax_bracket_22(self):
        self.assertEqual(28179, bracket.calculate_tax(165000))

    def test_tax_bracket_24(self):
        self.assertEqual(64179, bracket.calculate_tax(315000))

    def test_tax_bracket_32(self):
        self.assertEqual(91379, bracket.calculate_tax(400000))

    def test_tax_bracket_35(self):
        self.assertEqual(161379, bracket.calculate_tax(600000))

    def test_tax_bracket_37(self):
        self.assertEqual(309379, bracket.calculate_tax(1000000))

    def test_tax_bracket_handles_empty_bracket_gracefully(self):
        bracket = Bracket('Empty', [])
        self.assertEqual(0, bracket.calculate_tax(100000))
        
    def test_tax_bracket_at_various_salaries(self):
        self.assertEqual(2619, bracket.calculate_tax(25000))
        self.assertEqual(5619, bracket.calculate_tax(50000))
        self.assertEqual(13879, bracket.calculate_tax(100000))
        self.assertEqual(24879, bracket.calculate_tax(150000))
        self.assertEqual(36579, bracket.calculate_tax(200000))
        self.assertEqual(60579, bracket.calculate_tax(300000))


if __name__ == '__main__':
    unittest.main()
