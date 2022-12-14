class Solution:
    def rob(self, nums: List[int]) -> int:
        count = len(nums)
        if count == 0:
            return 0
        elif count == 1:
            return nums[0]
        elif count == 2:
            return max(nums[0], nums[1])
        memo = nums[:]
        memo[1] = max(nums[0], nums[1])
        for i in range(2, count):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
        return memo[count - 1]