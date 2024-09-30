class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxsize = maxSize
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == self.maxsize:
            return
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(0, k):
            if len(self.stack) == i:
                return
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
