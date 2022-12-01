class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half1, half2 = 0, 0
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for i in range(len(s)):
            char = s[i]
            if char in vowels:
                if i < (len(s) // 2):
                    half1 += 1
                else:
                    half2 += 1

        return True if half1 == half2 else False
