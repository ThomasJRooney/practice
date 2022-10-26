#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    combos = []
    ret = 0
    for i in range(2, len(s)):
        for combo in list(combinations(s, i)):
            combos.append(combo)
    for combo in combos:
        b = True
        for i in range(len(combo)):
            for j in range(i, len(combo)):
                if (combo[i] + combo[j]) % k == 0:
                    b = False
        if b:
            ret = max(ret, len(combo))
    return ret


    print(combos)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
