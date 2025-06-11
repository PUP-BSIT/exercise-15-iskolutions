from iskolutions import causon, franco, efondo, lopez
from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6

def display_get_choice():
    print("============Select an Option============")
    print("1. Miko Lorenz O. Causon")
    print("2. Fernette Pearl M. Franco")
    print("3. Aaron Kyle D. Efondo")
    print("4. Jakim D. Lopez")
    print("5. Exit")
    print("========================================")
    
    try:
        choice = int(input("Enter your choice: "))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input! Please enter a number.")
        return UNSET_OPTION

def process_choice(choice):
    match choice:
        case 1:
            dice_roller = causon.DiceRoller()
            dice_roller.menu()
        case 2:
            franco_calculator = franco.FrancoCalculator()
            franco_calculator.menu()
        case 3:
            user_nickname = input("Enter your nickname: ")
            budget_tracker = efondo.BudgetTracker(user_nickname)
            budget_tracker.menu()
        case 4:
            lopez_game = lopez.TypeMemorizePup()
            lopez_game.menu()
        case 5:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")

def main():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)

main()