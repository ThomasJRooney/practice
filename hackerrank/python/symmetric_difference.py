a = input()
a = set(map(int, input().split()))
b = input()
b = set(map(int, input().split()))
ab = list(a.difference(b)) + list(b.difference(a))
ab.sort()
for i in ab:
    print(i)
