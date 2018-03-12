import sys
from source.tax_bracket import Bracket, BracketElement

# This is the 2018 Married filing joint tax bracket.
federal_bracket = Bracket(
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

# This is the 2018 KY State tax bracket for all filers.
state_bracket = Bracket(
    '2018 KY Taxes - All Filers',
    [
        BracketElement('2%', 0, 3000, 0.02),
        BracketElement('3%', 3001, 4000, 0.03),
        BracketElement('4%', 4001, 5000, 0.04),
        BracketElement('5%', 5001, 8000, 0.05),
        BracketElement('5.8%', 8001, 75000, 0.058),
        BracketElement('6%', 75001, sys.maxsize, 0.06),
    ]
)

# Example salary
salary = 100000

# Todo: Add support for accumulating deductions
fed_deductions = 24000
state_deductions = 24000

# Calculate federal and state taxes using the brackets.
fed_taxes = federal_bracket.calculate_tax(salary - fed_deductions)
state_taxes = state_bracket.calculate_tax(salary - state_deductions)

print("----------------------------------------------------------------------------")
print("Salary = ${0:,.2f}".format(salary))
print("Federal Tax = ${0:,.2f}".format(fed_taxes))
print("State Tax = ${0:,.2f}".format(state_taxes))
print("Total Taxes: ${0:,.2f}".format(fed_taxes + state_taxes))
print("Effective Tax Rate: {0:,.2%}".format((fed_taxes + state_taxes)/salary))
print("----------------------------------------------------------------------------")
