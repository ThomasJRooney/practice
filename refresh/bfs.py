class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            cur = queue.pop()
            array.append(cur.name)
            for child in cur.children:
                queue.insert(0, child)
        return array
