'''
    To run the main file use the command line

    For help:
        python main.py -h

    Example:
        python main.py 8 BFS
'''

import argparse

from Problem import Problem
from Algorithms import *


# Display into command line
description = 'Solve the NQueen problem using BFS'
N_helper = 'Value for N in Nqueen problem default it 4'
Algo_helper = 'Algorithm used to solve the NQueen problem'
choices = ['BFS', 'IDS', 'GA']
args = ['N', 'Algorithm']

parser = argparse.ArgumentParser(description=description)
parser.add_argument(args[0], nargs='?', type=int, default=4, help=N_helper)
parser.add_argument(args[1], choices=choices, type=str.upper, help=Algo_helper)


# Get arguments from the user
args = parser.parse_args()


# use the arguments to solve the NQueen problem
problem = Problem(args.N)
solution = []
is_supported = False

if args.Algorithm == 'BFS':
    is_supported = True
    solution = BFS(problem)

if is_supported:
    problem.print_board(solution)
else:
    print('Not supported yet')