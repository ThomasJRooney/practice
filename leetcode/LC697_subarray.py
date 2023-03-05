class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic, max_degree, res = collections.defaultdict(list), 0, float('inf')
        for i in range(len(nums)):
            dic[nums[i]].append(i + 1)
            max_degree = max(len(dic[nums[i]]), max_degree)
        if max_degree == 1: return 1
        for i in dic:
            if len(dic[i]) == max_degree:
                res = min(res, dic[i][-1] - dic[i][0] + 1)
        return res