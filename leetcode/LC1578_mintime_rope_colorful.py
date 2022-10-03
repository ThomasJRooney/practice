'''
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
'''

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        bday = []
        for i in range(len(colors)):
            if bday and colors[i] == colors[bday[-1]]:
                if neededTime[i] < neededTime[bday[-1]]:
                    cost += neededTime[i]
                else:
                    cost += neededTime[bday[-1]]
                    bday.append(i)
            else:
                bday.append(i)
        return cost