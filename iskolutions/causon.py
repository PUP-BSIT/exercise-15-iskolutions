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