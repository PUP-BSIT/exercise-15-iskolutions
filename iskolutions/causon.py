from os import system

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