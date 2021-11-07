from Node import Node

class Problem:
    def __init__(self):
        self.actions = ['R', 'L', 'U', 'D']

        # Fully observable environment =)
        # BFS يتعامل مع بيئة واضحة
        # لازم نخزن البيئة عشان نستخدمها عند البحث
        self.maze = [
            ["#", "#", "#", "#", "#", "I", "#", "#", "#"], # i
            ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", " ", " ", "#", " ", "#"],
            ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
            ["#", " ", " ", " ", "#", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#", " ", " ", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "G", "#"], 
              # j
        ]  # من دون البيئة هذا ما راح نقدر نتوصل الى حل

        self.initial_state, self.goal_state = self.get_init()

    def get_init(self):
        # نبحث على نقطة البداية و الهدف
        for idx, row in enumerate(self.maze):
            if "I" in row:
                c_node = Node(idx, row.index("I")) # Inital state
            if "G" in row:
                g_node = Node(idx, row.index("G"))  # Goal state
        
        return c_node, g_node


    def goal_test(self, node):
        return node == self.goal_state

    def print_maze(self, path):
        if isinstance(path, str): print(path)
        else:
            # نطبع البيئة
            for i, row in enumerate(self.maze):
                for j, cell in enumerate(row):
                    if (i, j) in path:
                        print('+ ', end="")
                    else:
                        print(cell + " ", end="")
                print()

            print("Steps taken: ", len(path))