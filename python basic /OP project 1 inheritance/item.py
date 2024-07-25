class Item:
    all = []  # Class variable to hold all instances
    pay_rate = 0.8  # Class level attribute for discount

    def __init__(self, name: str, cost: int, quantity: int):
        assert cost > 0, f"Cost {cost} should be greater than zero!"
        assert quantity > 0, f"Quantity {quantity} should be greater than zero!"
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.cost}, {self.quantity})"

    def calculate(self):
        return self.cost * self.quantity

    def apply_disc(self):
        self.cost *= self.pay_rate
        return self.cost

