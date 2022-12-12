from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        res, two = 0, n // 2
        for i in range(two + 1):
            twos = i
            ones = n - (twos * 2)
            res += factorial(twos + ones) / (factorial(twos) * factorial(ones))
        return int(res)
