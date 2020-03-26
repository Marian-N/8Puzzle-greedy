from puzzle_functions import find_box

def wrong_boxes_count(puzzle, puzzle_goal):
    #This function counts how many boxes are in wrong position
    count = 0
    for row in range(len(puzzle)):
        for column in range(len(puzzle[0])):
            if(puzzle[row][column] != puzzle_goal[row][column]):
                count += 1
    return count

def distance_heuristic(puzzle, puzzle_goal):
    #This function counts how many steps does each box need to take to be in correct place
    result = 0
    for row in puzzle:
        for box in row:
            goal_box = find_box(puzzle_goal, box)
            puzzle_box = find_box(puzzle, box)
            distances = [abs(abs(x) - abs(y)) for x, y in zip(goal_box, puzzle_box)]
            for value in distances:
                result += value
    return result

def cost(puzzle, puzzle_goal, heuristic):
    #This function returns cost of heuristic 1, 2 or 3(combination of 1 and 2)
    if(heuristic == 1):
        return wrong_boxes_count(puzzle, puzzle_goal)
    elif(heuristic == 2):
        return distance_heuristic(puzzle, puzzle_goal)
    else:
        return wrong_boxes_count(puzzle, puzzle_goal) + distance_heuristic(puzzle, puzzle_goal)