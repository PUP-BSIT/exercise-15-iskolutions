import os

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

    def menu(self):
        while True:
            self.clear_screen()
            print("=== Franco Calculator Menu ===")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Power")
            print("6. Back to Main Menu")

            choice = input("Choose operation: ")

            if choice == '6':
                break

            if choice in ['1', '2', '3', '4', '5']:
                self.input_numbers()

                if choice == '1':
                    self.add()
                elif choice == '2':
                    self.subtract()
                elif choice == '3':
                    self.multiply()
                elif choice == '4':
                    self.divide()
                elif choice == '5':
                    self.power()

                input("\nPress Enter to continue...")
            else:
                print("Invalid choice. Try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    calculator = FrancoCalculator()
    calculator.menu()