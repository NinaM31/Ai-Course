import heapq as hq

from utils import child_node, obst_in_path, FAIL


def ASTAR(problem, r_obst=0):
    '''
        problem: Problem
        r_obst: int (optional parameter)

        This method calls the private function __ASTAR and displays its result
        It always shows the result when no obstacle is removed
    '''
    if r_obst > 0:
        # With r_obst or less removed
        path_obst = __ASTAR(problem, r_obst)
        problem.print_map(path_obst, r_obst)
        return path_obst
    else:
        # With no obstacles removed
        path_0 = __ASTAR(problem, 0)
        problem.print_map(path_0, 0)
            
        return path_0

def __ASTAR(problem, r_obst):
    '''
        problem: Problem
        r_obst: int

        This method uses A Star algorithm to find the shortest path to the princess

        return: list | the path from start to princess if faliure returns FAIL
    '''
    # get the initial coordinate
    c_node = problem.initial_state
 
    # initialize the frontier and store the path
    frontier = []

    # f(n) = g(n) + h(n) is the value of our priority queue
    fn = 0 + manhattan_distance(problem.goal_state, c_node)
    hq.heappush(frontier, (fn, [c_node] ) )

    while len(frontier) > 0:
        # lowest f(n) and corresponding item will be poped
        fn_1, c_path = hq.heappop(frontier)

        # get the tail of the path
        c_node = c_path[-1]

        # check if the tail reached the princess 
        if problem.goal_test(c_node):
            # If the first path found by ASTAR satisfies the amount of paths removed then return it
            if r_obst >= obst_in_path(c_path, problem.obstacles):
                return c_path

        # h(c_node)
        hn_1 = manhattan_distance(problem.goal_state, c_node)

        # for each neighboring path
        for action in problem.actions:
            child = child_node(problem, c_node, action)
            if not child: continue

            # g(n) = f(c_path) - h(c_node) 
            gn = ( fn_1 - hn_1 ) + 1

            if child not in c_path:
                # If the path is not explored add it
                path = c_path[:]
                path.append(child)

                if obst_in_path(path, problem.obstacles) > r_obst : continue
                
                hn = manhattan_distance(problem.goal_state, child)
                fn = hn + gn
                hq.heappush(frontier, (fn, path) )
    else:
        return FAIL

def manhattan_distance(a, b):
    '''
        a: tuple
        b: tuple

        This method is the heuristic function using the manhattan distance

        return int
    '''
    d1 = abs(a[0] - b[0])
    d2 = abs(a[1] - b[1])
    return d1 + d2