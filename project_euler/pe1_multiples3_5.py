#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = 3
    rSum = 0
    while(x < n):
        if x % 3 == 0 or x % 5 == 0:
            rSum += x
        if (x + 1) % 3 == 0 or (x + 1) % 5 == 0:
            x += 1
        elif (x + 2) % 3 == 0 or (x + 2) % 5 == 0:
            x += 2
        elif (x + 3) % 3 == 0 or (x + 3) % 5 == 0:
            x += 3
    print(rSum)
