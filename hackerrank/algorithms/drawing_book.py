#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    front = [0, 1]
    front_count = 0
    back = [n, n + 1]
    back_count = 0
    if n % 2 != 0:
        back = [n - 1, n]
    while True:
        if p in front: return front_count
        if p in back: return back_count
        
        front_count += 1
        back_count += 1
        front = [front[0] + 2, front[1] + 2]
        back = [back[0] - 2, back[1] - 2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()