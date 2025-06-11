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
    
    def view_balance(self):
        system("cls")
        print("\n--- Current Balance ---")
        print(f"Your Current balance is: ${self.balance:.2f}")
        input("\nPress enter to continue...")

    def view_transactions(self):
        system("cls")
        print("\n--- Transaction History ---")

        if not self.transactions:
            print("No transactions recorded yet.")
            input("\nPress enter to continue...")
            return
        
        count = 1
        for transaction in self.transactions:
            transaction_type = transaction[0]
            amount = transaction[1]
            print(f"{count}. {transaction_type}: ${amount:.2f}")
            count += 1
        
        input("\nPress enter to continue...")

    def reset_budget(self):
        system("cls")
        print("\n--- Reset Budget ---")
        confirmation = input("Do you want to reset tracker? (y/n): ").lower()

        if confirmation == 'y':
            self.balance = MIN_AMOUNT
            self.transactions.clear()
            print("\nBudget has been reset.")
            input("Press enter to continue...")
        else:
            print("\nCancelled. Budget was not reset.")
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
            self.add_income()
        elif choice == 2:
            self.add_expense()
        elif choice == 3:
            self.view_balance()
        elif choice == 4:
            self.view_transactions()
        elif choice == 5:
            self.reset_budget()
        elif choice == 6:
            print("\nReturning to main menu...")
            input("Press enter to continue...")
            return True  #Exit menu loop
        else:
            print("\nInvalid choice. Try again.")
            input("Press enter to return...")
            
        return False  #Continue menu loop
    
    def menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_choice()
            self.process_choice(choice)