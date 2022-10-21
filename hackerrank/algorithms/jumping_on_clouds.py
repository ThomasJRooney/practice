#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    idx, newidx, e = 0, -1, 100
    while newidx != 0:
        if newidx == -1:
            newidx = (idx + k) % len(c)
        else:
            newidx = (newidx + k) % len(c)
        e -= 1
        if c[newidx] == 1:
            e -= 2
    return e



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
