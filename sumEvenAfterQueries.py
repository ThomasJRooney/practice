'''
You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.
'''

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ret = []
        evenSum = 0
        for n in nums:
            if n % 2 == 0:
                evenSum += n
        for val, idx in queries:
            num = nums[idx]
            wasEven = False
            isEven = False
            if num % 2 == 0:
                wasEven = True
            if (num + val) % 2 == 0:
                isEven = True
            
            if wasEven and not isEven:
                evenSum -= num
            elif not wasEven and isEven:
                evenSum += num + val
            elif wasEven and isEven:
                evenSum += val
            nums[idx] += val 
            ret.append(evenSum)
        return ret
