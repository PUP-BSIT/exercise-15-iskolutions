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
