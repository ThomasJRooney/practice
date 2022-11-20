class Solution:
    def countAndSay(self, n: int) -> str:
        sep = {"12" : "1|2", "21" : "2|1", "13" : "1|3", "31" : "3|1", "23" : "2|3", "32" : "3|2"}
        say = "1"
        for _ in range(n - 1):
            for w, r in sep.items(): say = say.replace(w, r)
            say = "".join([f"{len(b)}{b[0]}" for b in say.split("|")])
        return say
