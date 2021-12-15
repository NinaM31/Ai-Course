import os 

from helper import resource_path

class Problem:
    def __init__(self, filename):
        # All the action the Knight can do
        self.actions = ['R', 'L', 'U', 'D']

        # Reading the Map floor file
        self.read_file(filename)   

    def read_file(self, filename):
        ''' 
            filename: string 

            This method is responsible for extracting data from txt
        '''
        # Preforming a absolute file read
        dirname = os.path.dirname(__file__)
        file = os.path.join(dirname, filename)

        with open(resource_path(file)) as f:
            # each line stored as an element
            lines = f.readlines() 
            data = []
            
            # for each element in lines remove space transform to int and store as tuple coordinate
            for i, l in enumerate(lines):
                items = l.split(' ') 
                r = int(items[0])
                c = int(items[1])

                data.append( (r, c) )

            # Use the data extraxted to create the dungeon
            self.create_dungeon(data)
            
    def create_dungeon(self, data):
        ''' 
            data: array tuples 

            This method is responsible for using data to generate the dungeon floor map
            And initialize the initial coordinate and goal coordinate
        '''
        # The first coordinate is the dungeon size
        self.M, self.N = data[0]
        self.obstacles = data[1: ]

        # initialize the knight initial coordinate & goal coordinate
        self.initial_state = (0, 0)
        self.goal_state =  (self.M-1, self.N-1)
        self.create_map()

    def create_map(self):
        self.map = [['.'] * (self.N) for _ in range( (self.M) )]
        self.border = [['B'] * (self.N + 1) for _ in range( (self.M + 1) ) ]
        
        for i in range(self.M):
            for j in range(self.N):
                if (i, j) == self.initial_state:
                    self.map[i][j] = 'K'
                elif (i, j) in self.obstacles:
                    self.map[i][j] = 'X'
                elif (i, j) == self.goal_state:
                    self.map[i][j] = 'P'


    def goal_test(self, node):
        ''' 
            node: tuple

            This method will check if the node coordinates equals the goal coordinates

            return: bool
        '''
        return node ==  self.goal_state

    def print_map(self, path, r_obst=0):
        ''' 
            path: list | string
            r_bost: int
            
            This method will print the floor map with respect to the path taken by the knight
        '''

        # If there is no path notify with error
        if isinstance(path, str): print(f'{path}: when  obstacles removed {r_obst}')

        # If a path exist notify with the solution
        else:
            # for row and col
            for i in range(self.M):
                for j in range(self.N):
                    # Print the knight position | Princess
                    if (i,j) ==  self.initial_state: print('K ', end="")
                    elif (i,j) ==  self.goal_state: print('P ', end="")

                    # Print the position taken (.) | position blocked (X) | position empty (-)
                    elif (i,j) in path: print('. ', end="")
                    elif (i,j) in self.obstacles: print('X ', end="")
                    else: print("- ", end="")
                print()

            # This checks if this is an Input print or Output print
            # Input print: Show the map before solving
            # Output print: show map after solving            
            if len(path) > 0:
                # If Output print display the results
                print(f"Steps taken when {r_obst} or less obstacles removed = {len(path)-1} ")
                for p in path:
                    print(f'{p} -> ', end="")
        print()