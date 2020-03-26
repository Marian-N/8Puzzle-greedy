def find_box(puzzle, box):
    #Find position of value in array and return as array [x, y]
    position = [0, 0]

    for i in range(len(puzzle)):
        try:
            position[1] = puzzle[i].index(box)
            position[0] = i
            return position
        except:
            continue

def is_goal(puzzle, puzzle_goal):
    #Check if puzzle is in goal state
    for row in range(len(puzzle)):
        for column in range(len(puzzle[0])):
            if(puzzle[row][column] != puzzle_goal[row][column]):
                return False
    return True

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

def print_start_goal(puzzle, puzzle_goal):
    print("Goal puzzle:")
    print_puzzle(puzzle_goal)
    print("Puzzle to solve:")
    print_puzzle(puzzle)

def load_puzzle(file):
    puzzle = []

    try:
        file_path = file
        with open(file_path, "r") as file:
            file_content = file.read()
    except:
        print(f"File({file_path}) not found")
        return puzzle

    '''Removes "((" from start and "))" from end of string
    ((1 2 3)(4 5 6)(7 8 m)) -> 1 2 3)(4 5 6)(7 8 m'''
    file_content = file_content[2:len(file_content) - 2]
    file_content = file_content.replace("m", "0")

    '''Split string into array with )( as separator
    1 2 3)(4 5 6)(7 8 m - > ['1 2 3', '4 5 6', '7 8 m']'''
    file_content = file_content.split(")(")

    #Creates multi-dimensional array from array of strings
    for row in file_content:
        int_row = [int(x) for x in row.split()]
        puzzle.append(int_row)

    return puzzle