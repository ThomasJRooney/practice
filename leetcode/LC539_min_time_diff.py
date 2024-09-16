class Solution(object):
    def findMinDifference(self, timePoints):
        def timeToMinutes(time):
            hrs, mins = map(int, time.split(':'))
            return hrs * 60 + mins
        
        mins = [timeToMinutes(tp) for tp in timePoints]
        mins.sort()
        min_diff = float('inf')
        for i in range(1, len(mins)):
            min_diff = min(min_diff, mins[i] - mins[i - 1])
        
        circ_diff = 1440 - mins[-1] + mins[0]
        min_diff = min(min_diff, circ_diff)
        return min_diff
