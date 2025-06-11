from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6
MIN_AMOUNT = 0.0

class BudgetTracker:
    def __init__(self, name):
        self.name = name
        self.balance =  MIN_AMOUNT
        self.transactions = []