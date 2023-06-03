Select tags
0/5
from collections import defaultdict

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        def def_value():
            return 0
        game = defaultdict(def_value)

        ball, i = 1, 0
        while True:
            game[ball] += 1
            if game[ball] > 1: break
            i += 1
            ball = ((ball + (i * k)) % n)
            if ball == 0: ball = n
        
        losers = []
        for i in range(1, n + 1):
            if game[i] == 0: losers.append(i)
        return losers
