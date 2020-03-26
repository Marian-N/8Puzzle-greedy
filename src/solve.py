import time
from greedy import greedy
from puzzle_functions import print_start_goal, print_puzzle
from path import print_path

def solve(puzzle, puzzle_goal, heuristics):
    #Print time to solve puzzle with each heuristic, number of steps to take and give option to print all steps of solution
    #If you choose to print solution it will also create file with steps to solve puzzle
    solutions = list()
    solution_operators = list()
    for heuristic in heuristics:
        print(f"Solving puzzle with heuristic {heuristic}.")
        start_time = time.time()
        solution, operators = greedy(puzzle, puzzle_goal, heuristic)
        end_time = time.time()
        solution_time = end_time - start_time
        solutions.append(solution)
        solution_operators.append(operators)
        if(solution):
            print(f"Solution found in {solution_time} seconds.")
            print(f"Solution has {len(solution) - 1} steps.\n")
        else:
            print("Solution not found.")
            print(f"Elapsed time: {solution_time}")

    if(len(solutions) > 0 and None not in solutions):
        decision = 4
        while int(decision) > len(solutions):
            decision = input("Enter solution number to print solution(enter 0 to print all) or anything else to exit: ")
        print_start_goal(puzzle, puzzle_goal)
        if(decision == "1" or decision == "2" or decision == "3"):
            print_path(solutions[int(decision) - 1], solution_operators[int(decision) - 1], decision)
        elif(decision == "0"):
            for solution in range(len(solutions)):
                print("-------------------------------------")
                print_path(solutions[solution], solution_operators[solution], solution + 1)
                print("-------------------------------------")
                print_start_goal(puzzle, puzzle_goal)
    else:
        print("Found no solutions.")