import sys
class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)
		ans = 0
		diff = sys.maxsize

		for i in range(n):
			l , r = i + 1, n - 1

			while l < r:
				currSum = nums[i] + nums[l] + nums[r]

				if currSum == target:
					return currSum

				if currSum > target:
					r -= 1
				else:
					l += 1

				if abs(target - currSum) < diff:
					ans = currSum
					diff = abs(target - currSum)
		return ans
