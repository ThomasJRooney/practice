n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    a, b, x, y = l[0], l[1], l[2], l[3]
    a = a / x
    b = b / y
    if a == b:
        print("Both")
    elif a > b:
        print("Chefina")
    else:
        print("Chef")
