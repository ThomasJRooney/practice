class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for winner, loser in matches:
            if winner in dic:
                dic[winner][0] += 1
            else:
                dic[winner] = [1, 0]
            if loser in dic:
                dic[loser][1] += 1
            else:
                dic[loser] = [0, 1]
        answer = [[], []]
        for key in dic.keys():
            if dic[key][1] == 0:
                answer[0].append(key)
            if dic[key][1] == 1:
                answer[1].append(key)
        return [sorted(answer[0]), sorted(answer[1])]
