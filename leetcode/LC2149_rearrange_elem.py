class Solution(object):
    def rearrangeArray(self, nums):
        pos, neg, ret = [], [], []
        for n in nums:
            pos.append(n) if n > 0 else neg.append(n)
        for i in range(len(pos)):
            ret.append(pos[i])
            ret.append(neg[i])
        return ret
