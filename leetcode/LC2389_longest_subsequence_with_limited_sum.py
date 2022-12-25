class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:    
        nums.sort()
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)
        res = []
        for q in queries:
            i = bisect_right(preSum, q)
            res.append(i - 1)
        return res