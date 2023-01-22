class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        min_cost = float('INF')
        def get_cost(l):
            if l == []:
                return 0
            int_len, rem_count = len(l), 0
            for num in l:
                if l.count(num) == 1: rem_count += 1 
            return k + (int_len - rem_count)
        
        for x in range(len(nums)):
            first = nums[0:x]
            second = nums[x:len(nums)]
            min_cost = min(min_cost, get_cost(first) + get_cost(second))
        return min_cost