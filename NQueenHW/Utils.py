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
        # 1st queen place only on 1st row, 2nd queen placed only in second row
        if len(c_board_state) < i:
            break
        
        for j, _ in enumerate(row):
            # possible queen position
            q_pos = (i, j) 

            # if the possible position is safe append it to c_board_state as possible board state
            if problem.is_queen_safe(q_pos, c_board_state) and q_pos not in c_board_state:
                # tmp is a single possible state
                tmp = set()

                # add current queen positions    
                tmp |= c_board_state

                # add the new queen position
                tmp.add(q_pos)

                # append it to the list of possible states
                possible_board_state.append(tmp)
    
    return possible_board_state