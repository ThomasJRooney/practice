class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A + [0]
        stack = []
        res = 0
        for i in range(len(A)):
            while stack and A[i] < A[stack[-1]]:
                cur = stack.pop()
                left = stack[-1]
                right = i
                res += A[cur] * (right - cur) * (cur - left)
            stack.append(i)
        return res % (10**9 + 7)
