class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(n for n in nums if n % 2 == 0)
        ret = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            ret.append(evenSum)
        return ret
