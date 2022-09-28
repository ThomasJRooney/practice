# init approach: back tracking, only works on smaller inputs, horrid optimization for larger inputs and times out
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(part):
            if len(part) == 4 and sum(n for (n, i) in part) == target:
                add = list(n for (n, i) in part)
                add.sort()
                ret.append(add)
                return
            else:
                i_set = set()
                for n, i in part:
                    i_set.add(i)

                for i in range(len(nums)):
                    if i not in i_set:
                        part.append((nums[i], i))
                        add = []
                        for n, i in part:
                            add.append(n)
                        add.sort()
                        if add not in ret:
                            backtrack(part)
                        part.pop()
        backtrack([])
        return(ret)

# 2nd approach need to review
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            if i - 1 >= 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i + 1, n):
                if j - 1 != i and nums[j - 1] == nums[j]:
                    continue

                find = target - (nums[i] + nums[j])
                l, r = j+1, n-1

                while l < r:
                    x = nums[l] + nums[r]
                    prevl, prevr = nums[l], nums[r]

                    if x == find:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))

                        while l < r and nums[l] == prevl:
                            l += 1

                        while r > l and nums[r] == prevr:
                            r -= 1

                    else:
                        if x < find:
                            while l < r and nums[l] == prevl:
                                l += 1
                        else:
                            while r > l and nums[r] == prevr:
                                r -= 1
        return ans
