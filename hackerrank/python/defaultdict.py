from collections import defaultdict

nm = list(map(int, input().split()))
d = defaultdict(list)
for i in range(nm[0]):
    letter = input()
    d[letter].append(str(i + 1))

for i in range(nm[1]):
    letter = input()
    if len(d[letter]) > 0:
        print(" ".join(d[letter]))
    else:
        print(-1)
