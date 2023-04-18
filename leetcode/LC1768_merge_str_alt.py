class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        build = ""
        for i in range(len(word1)):
            if len(word2) > i: build += word1[i] + word2[i]
            else: build += word1[i]
        if len(word2) > len(word1): build += word2[len(word1):]
        return build