import unittest
import taxes as tax
import sys

# 2018 Married Filing Joint Bracket
bracket = tax.Bracket(
    '2018 Maried Filing Jointly',
    [
        tax.BracketElement('10%', 0, 19050, 0.10),
        tax.BracketElement('12%', 19051, 77400, 0.12),
        tax.BracketElement('22%', 77401, 165000, 0.22),
        tax.BracketElement('24%', 165001, 315000, 0.24),
        tax.BracketElement('32%', 315001, 400000, 0.32),
        tax.BracketElement('35%', 400001, 600000, 0.35),
        tax.BracketElement('37%', 600001, sys.maxsize, 0.37),
    ])

class MyTestCase(unittest.TestCase):
    def test_annual_tax_bracket_10(self):
        self.assertEqual(1905, bracket.annual_tax(19050))

    def test_annual_tax_bracket_12(self):
        self.assertEqual(8907, bracket.annual_tax(77400))

    def test_annual_tax_bracket_22(self):
        self.assertEqual(28179, bracket.annual_tax(165000))

    def test_annual_tax_bracket_24(self):
        self.assertEqual(64179, bracket.annual_tax(315000))

    def test_annual_tax_bracket_32(self):
        self.assertEqual(91379, bracket.annual_tax(400000))

    def test_annual_tax_bracket_35(self):
        self.assertEqual(161379, bracket.annual_tax(600000))

    def test_annual_tax_bracket_37(self):
        self.assertEqual(309379, bracket.annual_tax(1000000))

    def test_handles_empty_bracket_gracefully(self):
        bracket = tax.Bracket('Empty', [])
        self.assertEqual(0, bracket.annual_tax(100000))

if __name__ == '__main__':
    unittest.main()
