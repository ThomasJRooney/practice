nab = list(map(int, input().split()))
n, a, b = nab[0], nab[1], nab[2]
p1 = n - a
p2 = p1 - b
print(str(p1) + " " + str(p2))
