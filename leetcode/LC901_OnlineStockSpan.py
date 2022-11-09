class StockSpanner:
    def __init__(self):
        self.stack = [[inf,0]]

    def next(self, price: int) -> int:
        cur = self.stack[-1][1] + 1
        while price >= self.stack[-1][0]:
            self.stack.pop(-1)
        span = cur - self.stack[-1][1]
        self.stack.append([price, cur])
        return span
