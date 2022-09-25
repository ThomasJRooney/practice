class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = [self]
        while len(stack) > 0:
            current = stack.pop(0)
            array.append(current.name)
            for c in reversed(current.children):
                stack.insert(0, c)
        return array
