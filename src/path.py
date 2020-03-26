from puzzle_functions import print_puzzle

def print_path(path, operators, solution):
    #Print solution and save it to file
    f = open(f"solution{solution}.txt", "w").close() #Clear and create file
    f = open(f"solution{solution}.txt", "a")
    print(f"Solution number {solution}")
    f.write(f"Solution number {solution}\n");
    for index in range(2, len(path)):
        print(f"Step {index - 1} - {operators[-index]}")
        f.write(f"Step {index - 1} - {operators[-index]}\n")
        print_puzzle(path[-index])
    print(f"Step {index} - {operators[0]}")
    f.write(f"Step {index} - {operators[0]}\n")
    print_puzzle(path[0])

def get_path(state):
    #This function returns steps to solve puzzle
    path = list()
    operators = list()
    current_state = state
    while(current_state != None):
        path.append(current_state.puzzle)
        operators.append(current_state.last_operator)
        current_state = current_state.parent
    return path, operators