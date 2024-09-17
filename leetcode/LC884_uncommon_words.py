class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        word_count = Counter(s1.split() + s2.split())
        return [word for word in word_count if word_count[word] == 1]
