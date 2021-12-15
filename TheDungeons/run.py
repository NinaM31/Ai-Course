from problem import Problem
from BFS import BFS
from ASTAR import ASTAR


while True:
    # Get user input
    Algo = input('Pick an algorithm [BFS or ASTAR]: ').lower()
    File = input('File path: ')
    obst = int( input('Obstacles to remove: ') )

    # initialize the problem with the users file name
    problem = Problem(File)

    # Show the problem before solving it
    print('Inputs:')
    problem.print_map([])

    # Solve the problem
    print('Outputs:')
    if Algo == 'bfs': BFS(problem, obst)
    elif Algo == 'astar': ASTAR(problem, obst)

    a = input('do you want to exit? [Y, N] ').lower()

    if a == 'y':
        break