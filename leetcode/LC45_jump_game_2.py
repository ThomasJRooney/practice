class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        steps = [0]
        for i in range(nums[0]): steps.append(1)
        for i in range(1, n):
            len_steps = len(steps)
            if len_steps >= nums[i] + i + 1: i += 1
            elif len_steps < nums[i] + i + 1:
                for j in range(nums[i] + i - len_steps + 1): steps.append(steps[i] + 1)
        return steps[n - 1] 