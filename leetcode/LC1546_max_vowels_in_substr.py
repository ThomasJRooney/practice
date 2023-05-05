class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_vowels = cur_vowels = 0
        for i, c in enumerate(s):
            if i >= k and s[i - k] in vowels: cur_vowels -= 1
            if c in vowels: cur_vowels += 1
            max_vowels = max(max_vowels, cur_vowels)
        return max_vowels