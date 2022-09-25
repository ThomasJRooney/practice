'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        def backtrack(s, left, right):
            if len(s) == (2 * n):
                parens.append("".join(s))
                return
            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()
        backtrack([], 0, 0)
        return parens
