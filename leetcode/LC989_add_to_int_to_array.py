class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = ""
        for i in range(len(num)): n += str(num[i])
        res = str(int(n) + k)
        out = []
        for i in range(len(res)): out.append(int(res[i]))
        return out