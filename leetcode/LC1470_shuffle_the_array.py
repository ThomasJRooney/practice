class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n, 2*n):
            ret.append(nums[i - n])
            ret.append(nums[i])
        return ret   