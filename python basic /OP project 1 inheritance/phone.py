from item import Item
import csv


class Phone(Item):
    def __init__(self, name: str, cost: int, quantity: int, broken: int):
        super().__init__(name, cost, quantity)
        assert broken >= 0, f"Broken {broken} should be greater than or equal to zero!"
        self.broken = broken


