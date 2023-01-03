class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret = 0
        for i in range(len(strs[0])):
            x = []
            for s in strs:
                x.append(s[i])
            if sorted(x) != x:
                ret += 1
        return ret