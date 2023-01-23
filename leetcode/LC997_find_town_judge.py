class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust == []: return 1
        left, right = set(), set()
        judge = -1
        for l, r in trust:
            left.add(l)
            right.add(r)
        dif = right.difference(left)
        if len(dif) == 1:
            judge = list(dif)[0]
        else:
            return -1
        for i in range(1, n):
            if i != judge:
                if [i, judge] not in trust:
                    return -1
        return judge