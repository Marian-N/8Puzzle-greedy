from copy import deepcopy

class State:
    def __init__(self, puzzle, parent = None, last_operator = ""):
        self.puzzle = deepcopy(puzzle)
        self.parent = parent
        self.last_operator = last_operator