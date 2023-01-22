class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def palindrome(a):
            return a == a[::-1]
        def backtrack(i, cur):
            if i == len(s):
                ret.append(cur)
                return
            for j in range(i, len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    backtrack(j + 1, cur + [sol])
            return
        backtrack(0, [])
        return ret