from os import system
import random

DEFAULT_DICE = [1, 2, 3, 4, 5, 6]
DEFAULT_NUMBER_OF_DICE = 1
DEFAULT_HISTORY = []
DEFAULT_STATISTICS = {
    "Total Rolls": 0,
    "Total Score": 0
}
UNSET_OPTION = -1
EXIT_OPTION = 8

class DiceRoller:
    def __init__(self):
        self.dice = list(DEFAULT_DICE)
        self.roll_history = list(DEFAULT_HISTORY)
        self.statistics = dict(DEFAULT_STATISTICS)
    
    def get_yes_no_input(self, prompt):
        # Asks the user repeatedly until it answers 'yes' / 'y' or 'no' / 'n'
        while True:
            user_input = input(prompt).strip().lower()
            
            if user_input in ('yes', 'y'):
                return True
            
            if user_input in ('no', 'n'):
                return False
            
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    def roll_dice(self, number_of_dice):
        # Roll dice repeatedly until user says no.
        while True:
            # Roll and display
            system("cls")
            print("You rolled: ")
            rolled_dice = random.choices(self.dice, k=number_of_dice)
            self.roll_history.insert(0, rolled_dice) # Insert at index 0
            self.statistics["Total Rolls"] += 1
            self.statistics["Total Score"] += sum(rolled_dice)
            print("\t".join(map(str, rolled_dice)))
            
            # Ask to continue
            if not self.get_yes_no_input("\nRoll again? [yes/no]: "):
                # Stop if user says no
                break
            
        input("\nPress Enter to Continue...")
        
    def get_validated_number_input(self, prompt):
        system("cls")
        try:
            number_input = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            return None

        return number_input
        
    def roll_multiple_dice(self):
        # Prompt user for number of rolls until valid input is received.
        while True:
            prompt = "Enter how many dice to roll: "
            number_of_dice = self.get_validated_number_input(prompt)
            
            # End the loop if number is valid and positive
            if number_of_dice and number_of_dice > 0:
                self.roll_dice(number_of_dice)
                break
            
            print("Enter a positive number.")
    
    def set_dice(self):
        # Prompt user for the number of dice faces until it gets a valid input
        while True:
            system("cls")
            prompt = "Enter the number of sides the dice should have: "
            num_of_sides = self.get_validated_number_input(prompt)
            
            # Break the loop if the number is valid and positive
            if num_of_sides and num_of_sides >= 0:
                self.dice = list(range(1, num_of_sides + 1))
                break
            
            print("Please enter a valid, and positive number.")
     
    def view_history(self):
        system("cls")
        print("Roll History")
        
        for number, value in enumerate(reversed(self.roll_history), 1):
            print(f"Roll #{number}: {"\t".join(map(str, value))}")
        
        input("\nPress Enter to Continue.")
     
    def reset_history(self):
        system("cls")
        if self.get_yes_no_input("Would you like to reset the rolling history?" 
                               + " [yes/no]:"):
            self.roll_history = list(DEFAULT_HISTORY)
            print("Rolling history for this session has been reset.")
        else:
            print("History is not reset.")
            
        input("\nPress Enter to Continue.")
                
    def display_get_choice(self):
        system("cls")
        print("============RPG Game================")
        print("1. Roll!")
        print("2. Roll Multiple Dices")
        print("3. Edit Dice")
        print("4. View History")
        print("5. Reset History")
        print("6. View Statistics")
        print("7. Reset Statistics")
        print("8. Quit")
        print("====================================")
        
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Input a number!")
            input("\nPress Enter to Continue...")
            return UNSET_OPTION
    
    def evaluate_choice(self, choice):
        if choice == 1:
            self.roll_dice(DEFAULT_NUMBER_OF_DICE)
        elif choice == 2:
            self.roll_multiple_dice()
        elif choice == 3:
            self.set_dice()
        elif choice == 4:
            self.view_history()
        elif choice == 5:
            self.reset_history()
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            system("cls")
        else:
            print("Invalid Number! Pick a valid one.")
            input("\nPress Enter to Continue.")
    
    def menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            # display menu
            choice = self.display_get_choice()
            self.evaluate_choice(choice)
            
game = DiceRoller()
game.menu()