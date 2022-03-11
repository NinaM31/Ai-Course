'''
    This File contains the algorithms that will solve the NQueen problem.
    The algorithms are based on the Pseudocode in the Artificial Intelligence: A Modern Approach, Textbook.
    http://aima.cs.berkeley.edu/algorithms.pdf

    Algorithms (BFS, IDS, GA)

    Logic:
        Instead of searching where to place the queen, think of the problem as what are-
        the possible ways the board could looks like, and search for the-
        board that satisfies the goal state.
'''

from Utils import *


def BFS(problem):
    ''' 
        Following the BFS pseudocode in the textbook 
        Availablle: http://aima.cs.berkeley.edu/algorithms.pdf  Page5, Figure 3.9 (Breadth-first search)    
    '''

    # 1. get initial state
    init_board_state = problem.init_board_state

    # 2. create frontier and explored sets
    explorded_set = [] # empty
    frontier = [] # FIFO queue
    frontier.append(init_board_state)
    
    # 3. while True
    while True:

        # 4. check if frontier empty
        if len(frontier) == 0 : return 'No Solution'

        # 5. pop from FIFO and mark as explored
        c_board_state = frontier.pop(0) # FIFO
        explorded_set.append(c_board_state)

        # 6. Transition model
        for possible_board_state in expand(problem, c_board_state):
            
            # if an empty array returned then skip it
            if len(possible_board_state) == 0:
                continue

            # 6.1. check if already explored
            if possible_board_state not in explorded_set and possible_board_state not in frontier:
                # 6.2. check if goal state
                if problem.goal_test( possible_board_state ): 
                    return possible_board_state
                else:
                    frontier.append(possible_board_state)