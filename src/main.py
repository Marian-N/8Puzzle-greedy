from puzzle_functions import load_puzzle
from solve import solve

def main():
    puzzle = load_puzzle("Puzzles/3x3.txt") #Choose start state of puzzle
    puzzle_goal = load_puzzle(("Puzzles/3x3goal.txt")) #Chose goal state of puzzle
    heuristics = [1, 2, 3] #Choose which heuristics to use
    solve(puzzle, puzzle_goal, heuristics) #Solve with greedy algorithm

main()