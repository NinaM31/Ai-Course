bgn = "I"  # Initial state
end = "G"  # Goal state
actions = ['R', 'L', 'U', 'D']

# Fully observable environment =)
# BFS يتعامل مع بيئة واضحة
# لازم نخزن البيئة عشان نستخدمها عند البحث
maze = [
    ["#", "#", "#", "#", "#", bgn, "#", "#", "#"],  # i
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", end, "#"],
    # j
]  # من دون البيئة هذا ما راح نقدر نتوصل الى حل


class Node:
    def __init__(self, i, j, parent):
        self.i = i
        self.j = j
        self.parent = parent

    def __eq__(self, obj):
        return self.i == obj.i and self.j == obj.j


def print_maze(path):
    # نطبع البيئة
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path:
                print('+ ', end="")
            else:
                print(cell + " ", end="")
        print()

    print("Steps taken: ", len(path))


def solution(child):
    # Backtracking
    path = []
    while child:
        path.append((child.i, child.j))
        child = child.parent

    return path[::-1]


def child_node(c_node, action):
    child = None
    i, j = c_node.i, c_node.j

    if action == 'R':
        j = j + 1
        if j < len(maze[i]) and maze[i][j] != '#':
            child = Node(i, j, c_node)

    elif action == 'L':
        j = j - 1
        if j >= 0 and maze[i][j] != '#':
            child = Node(i, j, c_node)

    elif action == 'U':
        i = i - 1
        if i >= 0 and maze[i][j] != '#':
            child = Node(i, j, c_node)

    elif action == 'D':
        i = i + 1
        if i < len(maze[i]) and maze[i][j] != '#':
            child = Node(i, j, c_node)

    return child


def goal_test(g_node, c_node):
    return g_node == c_node


def BFS():
    # نبحث على نقطة البداية و الهدف
    for idx, row in enumerate(maze):
        if bgn in row:
            # Inital state
            c_node = Node(idx, row.index(bgn), None)
        if end in row:
            g_node = Node(idx, row.index(end), None)  # Goal state

    # نتئكد ان نقطة البداية لا تساوي الهدف
    if goal_test(g_node, c_node):
        return solution(c_node)

    open_set = []  # FIFO queue/ frontier
    explored_set = []

    open_set.append(c_node)

    while True:
        # لا يوجد حل
        if len(open_set) == 0:
            faliure = 'There is no availble path from {bgn} to {end}'
            return faliure

        c_node = open_set.pop(0)  # First in First out
        explored_set.append(c_node)

        for action in actions:
            child = child_node(c_node, action)
            if not child:
                continue

            if child not in explored_set or child not in open_set:
                if goal_test(g_node, child):
                    return solution(child)
                open_set.append(child)


path = BFS()
print_maze(path)
