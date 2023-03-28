class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        cur = n
        while cur != 1:
            if cur in visit: return False
            visit.add(cur)
            curstr = str(cur)
            cur = 0
            for n in curstr:
                cur += (int(n) * int(n))
        return True