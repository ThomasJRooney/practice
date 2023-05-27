class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n+1)
        i = n - 1
        while i >= 0:
            ans = -1001
            ans = max(ans, stoneValue[i] - dp[i+1])
            if i + 1 < n: ans = max(ans, stoneValue[i] + stoneValue[i+1] - dp[i+2])
            if i + 2 < n: ans = max(ans, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3])
            dp[i] = ans
            i-=1
        alice = dp[0]
        if alice > 0: return "Alice"
        elif alice < 0: return "Bob"
        else: return "Tie"