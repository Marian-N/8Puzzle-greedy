from copy import deepcopy

def down(puzzle, empty_box):
    #Get position of empty box
    row = empty_box[0]
    column = empty_box[1]
    new_state = deepcopy(puzzle)

    # If it is not possible to move down return 0
    if(row - 1 < 0):
        return 0

    #Change empty box with box above it
    new_state[row - 1][column], new_state[row][column] = new_state[row][column], new_state[row - 1][column]

    #If sucessful return 1
    return new_state

def up(puzzle, empty_box):
    #Get position of empty box
    row = empty_box[0]
    column = empty_box[1]
    new_state = deepcopy(puzzle)

    # If it is not possible to move up return 0
    if(row + 1 >= len(puzzle)):
        return 0

    #Change empty box with box bellow it
    new_state[row + 1][column], new_state[row][column] = new_state[row][column], new_state[row + 1][column]

    #If sucessful return 1
    return new_state

def right(puzzle, empty_box):
    # Get position of empty box
    row = empty_box[0]
    column = empty_box[1]
    new_state = deepcopy(puzzle)

    # If it is not possible to move right return 0
    if (column - 1 < 0):
        return 0

    # Change empty box with box left to it
    new_state[row][column - 1], new_state[row][column] = new_state[row][column], new_state[row][column - 1]

    # If sucessful return 1
    return new_state

def left(puzzle, empty_box):
    # Get position of empty box
    row = empty_box[0]
    column = empty_box[1]
    new_state = deepcopy(puzzle)

    # If it is not possible to move left return 0
    if (column + 1 >= len(puzzle[0])):
        return 0

    # Change empty box with box right to it
    new_state[row][column + 1], new_state[row][column] = new_state[row][column], new_state[row][column + 1]

    # If sucessful return 1
    return new_state