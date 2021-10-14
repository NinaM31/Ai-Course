class Node:
    def __init__(self, i, j, parent=None):
        self.i = i
        self.j = j
        self.parent = parent

    def __eq__(self, obj):
        return self.i == obj.i and self.j == obj.j