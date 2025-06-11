from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6
MIN_AMOUNT = 0.0

class BudgetTracker:
    def __init__(self, name):
        self.name = name
        self.balance =  MIN_AMOUNT
        self.transactions = []
    
    def display_choice(self):
        system("cls")
        print(f"\n========== {self.name}'s Budget Tracker ==========")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Reset Budget")
        print("6. Back to Main Menu")
    
        try:
            choice = int(input("Enter your choice: "))
            system("cls")
            return choice
        except ValueError:
            system("cls")
            print("Invalid input! Please enter a number.")
            return UNSET_OPTION