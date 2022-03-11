class Problem:

    def __init__(self, N):
        '''
            Initializes the NQueen problem
            Args:
                N: int -> chess board size N by N
        '''

        # 2 dim array with N col and N rows
        self.board = [['0'] * N for _ in range(N)] 
        self.N = N

        # initially empty
        self.init_board_state = []


    def is_queen_safe(self, q_pos, queens):
        '''
            Checks if the given position is safe to place a queen on it
            Args:
                q_pos : tuple  -> (row, col) on the board
                queens: array  -> array of all q_pos on the board
        '''
    
        for q2 in queens:
            if self.is_attacked(q_pos, q2): return False
        return True


    def is_attacked(self, q1, q2):
        '''
            checks if 2 queens attacked each other
            Args
                q1, q2: tuples -> the (row, col) of queens on board
        '''

        if q2[0] == q1[0]: return True # same row
        if q2[1] == q1[1]: return True # same col
        if abs(q2[0] - q1[0]) == abs(q2[1] - q1[1]): return True # same diagonal
        return False

    
    def goal_test(self, queens):
        '''
            Checks if the goal state is reached: All queens are on board and placed safely
            Args:
                queens: array -> array of q_pos(row, col) of each queen
        '''

        # check if N queens are on board
        if len(queens) < self.N:
            return False

        # check if any queen was attacked
        for i, q1 in enumerate(queens):
            for j, q2 in enumerate(queens):
                if i != j:
                    if self.is_attacked(q1, q2): return False
        
        # all queens are placed and non attacked
        return  True


    def print_board(self, queens):
        '''
            Print the board
            Args:
                queens: array -> array of q_pos(row, col) of each queen
        '''

        # if queens is a string then print it
        if isinstance(queens, str): print(queens)

        # else print the board
        else:
            for i, row in enumerate(self.board):
                for j, col in enumerate(row):
                    if (i, j) in queens:
                        print('Q ', end='')
                    else:
                        print(f'{col} ' , end='')
                print()
                
        print()