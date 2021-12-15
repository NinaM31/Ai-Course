from utils import child_node, obst_in_path, FAIL


def BFS(problem, r_obst):
    '''
        problem: Problem
        r_obst: int (optional parameter)

        This method calls the private function _+BFS and displays its result
        It always shows the result when no obstacle is removed
    '''
    if r_obst > 0:
        # With r_obst or less removed
        path_obst = __BFS(problem, r_obst)
        problem.print_map(path_obst, r_obst)
        return path_obst
    
    # With no obstacles removed
    path_0 = __BFS(problem, 0)
    problem.print_map(path_0, 0)

    return path_0

    
def __BFS(problem, r_obst):
    '''
        problem: Problem
        r_obst: int

        This method uses Breadth first search algorithm to find the shortest path to the princess

        return: list | the path from start to princess if faliure returns FAIL
    '''
    # get the initial coordinate
    c_path = problem.initial_state
    
    # check if this is the goal state
    if problem.goal_test(c_path):
        return [c_path]

    # initialize the frontier and store the path
    frontier = []
    frontier.append( [c_path] )

    while True:
        # check if the frontier is empty
        if len(frontier) == 0: return FAIL

        # Using FIFO to pop the first path
        c_path = frontier.pop(0)

        # get the tail of the path
        c_node = c_path[-1]
        
        # for each neighboring path
        for action in problem.actions: 
            child = child_node(problem, c_node, action) 

            if not child: continue # If None

            # Check if this path is Explored
            if child not in c_path:
                
                # If the path is not explored add it then check the goal and add to frontier
                path = c_path[:]
                path.append(child)

                if obst_in_path(path, problem.obstacles) > r_obst : continue
                
                if problem.goal_test(child):
                    # If the first path found by BFS satisfies the amount of paths removed then return it
                    if r_obst >= obst_in_path(path ,problem.obstacles):
                        return path

                # else add to frontier
                frontier.append(path) 