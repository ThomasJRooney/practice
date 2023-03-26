class MyQueue:

    def __init__(self):
        self.ins = []
        self.out = []

    def push(self, x):
        self.ins.append(x)

    def pop(self):
        self.peek()
        return self.out.pop()

    def peek(self):
        if not self.out:
            while self.ins:
                self.out.append(self.ins.pop())
        return self.out[-1]

    def empty(self):
        return not self.ins and not self.out