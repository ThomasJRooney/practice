class Solution(object):
    def minSwaps(self, s):
        ans = 0
        for c in s:
            if c == "[":
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2
        
