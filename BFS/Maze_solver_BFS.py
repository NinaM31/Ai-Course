from Node import Node
from MazeProblem import Problem


def BFS(problem):
    c_node = problem.initial_state

    if problem.goal_test(c_node):
        return solution(c_node)

    frontier = []  # FIFO queue/ frontier
    explored_set = []

    frontier.append(c_node)

    while True:
        # لا يوجد حل
        if len(frontier) == 0:
            faliure = 'There is no availble path'
            return faliure

        c_node = frontier.pop(0)  # First in First out
        explored_set.append(c_node)

        for action in problem.actions:
            child = child_node(problem, c_node, action)
            if not child: continue

            if child not in explored_set and child not in frontier:
                if problem.goal_test(child):
                    return solution(child)
                frontier.append(child)


def solution(child):
    # Backtracking
    path = []
    while child:
        path.append((child.i, child.j))
        child = child.parent

    return path[::-1]


def child_node(problem, c_node, action):
    child = None
    i, j = c_node.i, c_node.j

    if action == 'R':
        j = j + 1
        if j < len(problem.maze[i]) and problem.maze[i][j] != '#':
            child = Node(i, j, c_node)

    elif action == 'L':
        j = j - 1
        if j >= 0 and problem.maze[i][j] != '#':
            child = Node(i, j, c_node)

    elif action == 'U':
        i = i - 1
        if i >= 0 and problem.maze[i][j] != '#':
            child = Node(i, j, c_node)

    elif action == 'D':
        i = i + 1
        if i < len(problem.maze) and problem.maze[i][j] != '#':
            child = Node(i, j, c_node)

    return child


problem = Problem()
path = BFS(problem)
problem.print_maze(path)
