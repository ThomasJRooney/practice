import math
n = int(input())
for i in range(n):
    nx = list(map(int, input().split()))
    n, x = nx[0], nx[1]
    pizzas = (n * x) / 4
    print(math.ceil(pizzas))
