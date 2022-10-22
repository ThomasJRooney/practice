#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    if k == 0: return "Yes" if s == t else "No"
    if len(s) + k > len(t): return appendAndDelete(s[:-1], t, k - 1)
    return "Yes" if len(s) + k == len(t) and t.startswith(s) else "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
