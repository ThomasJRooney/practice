#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    bmin, bmax = scores[0], scores[0]
    out = [0, 0]
    for i in range(1, len(scores)):
        if scores[i] > bmax:
            out[0] += 1
            bmax = scores[i]
        if scores[i] < bmin:
            out[1] += 1
            bmin = scores[i]
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
