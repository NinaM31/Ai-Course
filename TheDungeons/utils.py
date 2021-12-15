FAIL = 'There is no availble path consider removing more obstacles'
def obst_in_path(path, obstacles):
    '''
        path: list
        obstacles: list

        This method check how many obstacles in the path

        return: int | number of obstacles in path
    '''
    num = 0
    for obstacle in obstacles:
        if obstacle in path:
            num += 1

    return num
        
def child_node(problem, c_node, action):
    '''
        problem: Problem
        c_node: tuple
        action: str
        
        This method is the transition function

        return: tuple | neighboring coordinates
    '''
    child = None
    i, j = c_node[0], c_node[1]
    parent = c_node

    if action == 'R':
        j = j + 1
        if j < problem.N:
            child = (i, j)

    elif action == 'L':
        j = j - 1
        if j >= 0 :
            child = (i, j)

    elif action == 'U':
        i = i - 1
        if i >= 0 :
            child = (i, j)

    elif action == 'D':
        i = i + 1
        if i < problem.M :
            child = (i, j)
    return child