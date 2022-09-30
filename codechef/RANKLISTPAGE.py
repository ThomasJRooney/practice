n = int(input())
for i in range(n):
    num = int(input())
    a = 0
    if num % 25 != 0:
        a += 1
    print((num // 25) + a)
