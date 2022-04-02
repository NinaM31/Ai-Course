'''
    This File contains the algorithms that will solve the NQueen problem.
    The algorithms are based on the Pseudocode in the Artificial Intelligence: A Modern Approach, Textbook.
    from yanshengjia https://github.com/yanshengjia/ml-road/blob/master/resources/Artificial%20Intelligence%20-%20A%20Modern%20Approach%20(3rd%20Edition).pdf

    Algorithms (BFS, IDS, A*, GA)

    Logic:
        Instead of searching where to place the queen, think of the problem as what are-
        the possible ways the board could look like, and search for the-
        board that satisfies the goal state.
'''

from Utils import *


def BFS(problem):
    ''' Following the BFS pseudocode in the textbook page 82'''

    # 1. get initial state
    init_board_state = problem.init_board_state

    # 2. create frontier and explored sets
    explorded_set = [] # empty
    frontier = [] # FIFO queue
    frontier.append(init_board_state)
    
    # 3. while True
    while True:

        # 4. check if frontier empty
        if len(frontier) == 0 : return 'failure'

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


def  IDS(problem):
    ''' Following the IDS pseudocode in the textbook page 89'''
    depth = 0
    while True:
        result = DLS(problem, depth)
        if result != 'cutoff': return result
        depth += 1


def DLS(problem, limit):
    return RDLS(problem.init_board_state, problem, limit)


def RDLS(c_board_state, problem, limit):
    # Base Case
    if problem.goal_test(c_board_state): return c_board_state
    elif limit == 0: return 'cutoff'

    else:
        cutoff_occurred = False
        # Transition model
        for possible_board_state in expand(problem, c_board_state):

            # if an empty array returned then skip it
            if len(possible_board_state) == 0:
                continue
            
            # Recursive case which can be [failure, cutoff or solution]
            result = RDLS(possible_board_state, problem, limit-1)

            # mark cutoff
            if result == 'cutoff': cutoff_occurred = True

            # return solution
            elif result != 'failure': return result
        
        if cutoff_occurred: return 'cutoff' 
        return 'failure'