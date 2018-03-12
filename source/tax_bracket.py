
class BracketElement:
    '''
    Single tax bracket element. Able to calculate the taxes due for the bracket entry
    it represents given a dollar amount.
    '''
    def __init__(self, name='0%', start=0, end=0, rate=0.0):
        self.name = name
        self.start = start
        self.end = end
        self.rate = rate

    def calculate(self, amount):
        if amount > self.end:
            return (self.end - self.start + 1) * self.rate
        elif amount >= self.start:
            return (amount - self.start + 1) * self.rate
        else:
            return 0

class Bracket:
    '''
    Holds a complete tax bracket and provides useful functions for working with that tax bracket.
    '''
    def __init__(self, name='bracket', bracket_elements=[]):
        self.name = name
        self.bracket_elements = bracket_elements

    def calculate_tax(self, amount):
        tax = 0
        for b in self.bracket_elements:
            tax = tax + b.calculate(amount)
        return round(tax)
