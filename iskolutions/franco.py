import os

UNSET_OPTION = -1
EXIT_OPTION = 6

class FrancoCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def clear_screen(self):
        os.system("cls")

    def input_numbers(self):
        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            self.input_numbers()

    def add(self):
        self.result = self.num1 + self.num2
        self.display_result()

    def subtract(self):
        self.result = self.num1 - self.num2
        self.display_result()

    def multiply(self):
        self.result = self.num1 * self.num2
        self.display_result()

    def divide(self):
        if self.num2 != 0:
            self.result = self.num1 / self.num2
        else:
            print("Error: Division by zero.")
            self.result = None

        self.display_result()

    def power(self):
        self.result = self.num1 ** self.num2
        self.display_result()

    def display_result(self):
        print("\n[Result]")
        if self.result is not None:
            print(f"{self.num1} and {self.num2} → Result: {self.result}")
        else:
            print("No result to display.")

    def process_choice(self, choice):
        if choice == 1:
            self.input_numbers()
            self.add()
        elif choice == 2:
            self.input_numbers()
            self.subtract()
        elif choice == 3:
            self.input_numbers()
            self.multiply()
        elif choice == 4:
            self.input_numbers()
            self.divide()
        elif choice == 5:
            self.input_numbers()
            self.power()
        elif choice == 6:
            input("Press enter to continue...")
            return True  #Exit menu loop
        else:
            print("\nInvalid choice. Try again.")
            input("Press enter to return...")
        return False  #Continue menu loop
    
    def display_choice(self):
        os.system("cls")
        print(f"=== Franco Calculator Menu ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))
            os.system("cls")
            return choice
        except ValueError:
            os.system("cls")
            print("Invalid input! Please enter a number.")
            return UNSET_OPTION
        
    def run_menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_choice()
            self.process_choice(choice)