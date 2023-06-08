class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def subset(p, up):
            if len(up) == 0:
                ret.append(p)
                return
            ch = up[0]
            for i in range(len(p) + 1): subset(p[0:i] + [ch] + p[i:], up[1:])
        subset([], nums)
        return ret