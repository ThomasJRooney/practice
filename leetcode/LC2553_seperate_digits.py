class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(x) for num in nums for x in str(num)]