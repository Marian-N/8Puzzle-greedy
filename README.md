# 8Puzzle-greedy
Python script for solving [8-Puzzle game](https://en.wikipedia.org/wiki/Sliding_puzzle)
## Heuristics
1. Number of misplaced tiles
2. Manhattan distance
3. Combination of 1. and 2.
## How to run
Example:

**puzzle = load_puzzle("Puzzles/3x3.txt")** #Choose file with start state of puzzle

**puzzle_goal = load_puzzle("Puzzles/3x3.txt")** #Choose file with goal state of puzzle

**heuristics = [1, 2, 3]** #it can be [1] [2, 1] or any combination of numbers 1, 2 and 3

**solve(puzzle, puzzle_goal, heuristics)** #Solves puzzle with greedy algorithm

Example of input file:

**((1 8 2)(0 4 3)(7 6 5))** #0 is empty tile

You will be able to choose which solution you want to display and write to text file.
