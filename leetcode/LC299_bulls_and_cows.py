from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic, bulls = Counter(secret) - Counter(guess), 0
        for i in range(len(secret)): 
            if secret[i] == guess[i]: bulls += 1
        cows = len(secret) - sum(dic.values()) - bulls
        return str(bulls) + "A" + str(cows) + "B"