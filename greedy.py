from queue import PriorityQueue
from itertools import count
import copy
from state import State
from heuristics import cost
from moves import up, down, left, right
from puzzle_functions import find_box, is_goal
from path import get_path

def greedy(puzzle, puzzle_goal, heuristic):
    pq = PriorityQueue()
    visited = {}
    ''' Unique value for PQ because if there is equal priority of 2 items 
        PQ will try compare items in PQ and you cant compare classes so it will compare unique values'''
    unique = count()
    start_state = State(puzzle) #First state does not have parent state and last operator
    move_cost = cost(puzzle, puzzle_goal, heuristic) #Calculate cost with chosen heuristic
    pq.put(((move_cost, next(unique)), start_state)) #Insert first state into PQ
    while True:
        if pq.empty():
            print(f"Searched {next(unique)} states.")
            return None, None
        current_state = pq.get()[1] #Get state with lowest cost from PQ
        if is_goal(current_state.puzzle, puzzle_goal):
            print(f"Searched {next(unique)} states.")
            return get_path(current_state)
        hashable_puzzle = tuple([tuple(row) for row in current_state.puzzle])
        if hashable_puzzle not in visited:
            visited[hashable_puzzle] = hashable_puzzle
            empty_box = find_box(current_state.puzzle, 0)

            #Generate new states and add to pq if it is possible to move up, down, left, right
            next_puzzle = []
            if(current_state.last_operator != "down"):
                next_puzzle = up(current_state.puzzle, empty_box)
                if (next_puzzle):
                    next_state = State(next_puzzle, current_state, "up")
                    move_cost = cost(next_puzzle, puzzle_goal, heuristic)
                    pq.put(((move_cost, next(unique)), next_state))

            if (current_state.last_operator != "up"):
                next_puzzle = down(current_state.puzzle, empty_box)
                if (next_puzzle):
                    next_state = State(next_puzzle, current_state, "down")
                    move_cost = cost(next_puzzle, puzzle_goal, heuristic)
                    pq.put(((move_cost, next(unique)), next_state))

            if (current_state.last_operator != "right"):
                next_puzzle = left(current_state.puzzle, empty_box)
                if (next_puzzle):
                    next_state = State(next_puzzle, current_state, "left")
                    move_cost = cost(next_puzzle, puzzle_goal, heuristic)
                    pq.put(((move_cost, next(unique)), next_state))

            if (current_state.last_operator != "left"):
                next_puzzle = right(current_state.puzzle, empty_box)
                if (next_puzzle):
                    next_state = State(next_puzzle, current_state, "right")
                    move_cost = cost(next_puzzle, puzzle_goal, heuristic)
                    pq.put(((move_cost, next(unique)), next_state))