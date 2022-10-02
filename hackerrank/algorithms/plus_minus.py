#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for n in arr:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
