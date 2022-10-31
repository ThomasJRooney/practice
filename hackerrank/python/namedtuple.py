from collections import namedtuple
n, table = int(input()), namedtuple("table", input())
print(round(sum(int(table(*input().split()).MARKS) for i in range(n)) / n, 2))