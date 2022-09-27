'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(part):
            if len(part) == len(nums):
                ret.append(part.copy())
                return
            else:
                for n in nums:
                    if n not in part:
                        part.append(n)
                        backtrack(part)
                        part.pop()
        backtrack([])
        return ret
