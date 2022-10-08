n = int(input())
for i in range(n):
    length = int(input())
    num = int(input(), 2)
    max_int = 0
    max_outcome = 0
    for i in range(n):
        xor = num ^ (num // (2 ** i))
        if xor > max_outcome:
            max_outcome = xor
            max_int = i
    print(max_int)
