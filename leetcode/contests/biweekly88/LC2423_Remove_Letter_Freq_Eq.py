class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = [0] * len(word) 
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]
            fd = {}
            highest = 0
            for j in range(len(temp)):
                if temp[j] in fd:
                    fd[temp[j]] += 1
                else:
                    fd[temp[j]] = 1
                highest = max(highest, fd[temp[j]])
            ret = True
            for j in range(len(temp)):
                if fd[temp[j]] != highest:
                    ret = False
            if ret:
                return True
            counter = [0] * len(word)  
        return False