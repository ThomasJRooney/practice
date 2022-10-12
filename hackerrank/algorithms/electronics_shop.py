#!/bin/python3

import os
import sys
from itertools import combinations

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    options = [k + d for k in keyboards for d in drives if k + d <= b]
    return -1 if len(options) == 0 else max(options)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()