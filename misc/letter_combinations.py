class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index, path):
            if len(path) == len(digits):
                combos.append("".join(path))
                return
            letters = dic[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        combos = []
        backtrack(0, [])
        return combos
