class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]
        if n <= 2:
            return trib[n]
        for i in range(3, n + 1):
            next_trib = trib[-1] + trib[-2] + trib[-3]
            if i == n:
                return next_trib
            trib.append(next_trib)