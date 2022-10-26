class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            rem = total % k
            if rem not in remainder:
                remainder[rem] = i
            elif i - remainder[rem] > 1:
                return True
        return False
