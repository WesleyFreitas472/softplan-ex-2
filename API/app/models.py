

class Value:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def getValueWithTaxes(self, tax: float) -> float:
        return self.amount + (self.amount * tax / 100)