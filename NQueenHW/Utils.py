def expand(problem, c_board_state):
    '''
        get a list of possible places 1 queen can be placed
        Args:
            problem       : Problem -> the NQueen problem class
            c_board_state : array   -> array of current queen positions (row, col)
        Return:
            array of safe places to place the queens
    '''
    
    # array of possible board state when adding 1 queen to c_board_state
    possible_board_state = []

    # loop over the board
    for i, row in enumerate(problem.board):
        for j, _ in enumerate(row):
            # possible queen position
            q_pos = (i, j) 

            # if the possible position is safe append it to c_board_state as possible board state
            if problem.is_queen_safe(q_pos, c_board_state):
                # tmp is a single possible state
                tmp = []

                # add current queen positions
                for cq_pos in c_board_state:
                    tmp.append(cq_pos)

                # add the new queen position
                tmp.append(q_pos)

                # append it to the list of possible states
                possible_board_state.append(tmp)
    
    return possible_board_state


def not_in(part, whole):
    '''
        checks if the part does not exist in a whole
        Args:
            part : array -> array of tuples q_pos(row, col) [q1, q2, ...]
            whole: array -> array of array of typles        [ [q1, q2, ...], [q1, ..] ]

        Return:
            True or False: True if part not in whole
    '''
    ...