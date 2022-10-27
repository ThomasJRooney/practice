# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

date = list(map(int, input().split()))
num = calendar.weekday(date[2], date[0], date[1])
datemap = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}
print(datemap[num])
