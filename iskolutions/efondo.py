from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6
MIN_AMOUNT = 0.0

class BudgetTracker:
    def __init__(self, name):
        self.name = name
        self.balance =  MIN_AMOUNT
        self.transactions = []
    
    def add_income(self):
        system("cls")
        print("\n--- Add Income ---")
        amount = input("Enter income amount: $")
        
        try:
            amount = float(amount)
        except ValueError:
            print("\nInvalid input. Please enter a number")
            input("Press enter to return...")
            return

        if amount <= MIN_AMOUNT:
            print("\nAmount must be greater than 0.")
            input("Press enter to return...")
            return
        
        self.balance += amount 
        self.transactions.append(("Income", amount))
        print(f"\nIncome of ${amount:.2f} added successfully.")
        input("Press enter to continue...")
    
    def add_expense(self):
        system("cls")
        print("\n--- Add Expense ---")
        amount = input("Enter expense amount: $")
        
        try:
            amount = float(amount)
        except ValueError:
            print("\nInvalid input. Please enter a number")
            input("Press enter to return...")
            return
            
        if amount <= MIN_AMOUNT:
            print("\nAmount must be greater than 0.")
            input("Press enter to return...")
            return
        
        if amount > self.balance:
            print("\nNot enough balance for this expense")
            input("Press enter to return...")
            return
        
        self.balance -= amount
        self.transactions.append(("Expense", amount))
        print(f"\nExpense of ${amount:.2f} added successfully.")
        input("Press enter to continue...")

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
        
    def process_choice(self, choice):
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            print("\nReturning to main menu...")
            input("Press enter to continue...")
            return True  #Exit menu loop
        
        print("\nInvalid choice. Try again.")
        input("Press enter to return...")
        return False  #Continue menu loop
    
    def menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_choice()
            self.process_choice(choice)