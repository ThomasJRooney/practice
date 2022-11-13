#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    cols = math.ceil(math.sqrt(len(s)))
    grid = [''] * cols
    col = 0
    for i in range(len(s)):
        grid[col] += s[i]
        col += 1
        if col == cols:
            col = 0
    return ' '.join(grid)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
