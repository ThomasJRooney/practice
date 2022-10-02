#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    out = s[:8]
    if s[8:10] == "PM":
        if out[:2] != "12":
            out = str(int(out[:2]) + 12) + out[2:]
    else:
        if out[:2] == "12":
            out = "00" + out[2:]
    return(out)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
