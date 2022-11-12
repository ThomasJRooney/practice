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
    res = {i: 0 for i in range(k)}
    for i in s:
        res[i % k] += 1
    if res[0] > 1:
        res[0] = 1
    if k % 2 == 0 and res[ k // 2] > 1:
        res[k // 2] = 1
    for i in range(1, int(math.ceil(k / 2))):
        if res[i] == 0 or res[k - i] == 0:
            pass
        elif res[i] < res[k - i]:
            res[i] = 0
        else:
            res[k - i] = 0
    return sum(res.values())
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
