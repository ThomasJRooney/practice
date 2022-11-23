from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(len(nums) + 1):
            combos = combinations(nums, i)
            for combo in combos:
                if combo not in ret:
                    ret.append(combo)
        return ret
