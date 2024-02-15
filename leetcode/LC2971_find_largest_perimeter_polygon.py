class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        while len(nums) >= 3:
            if sum(nums[0:-1]) > nums[-1]:
                return sum(nums)
            else:
                nums = nums[0:-1]
        return -1
