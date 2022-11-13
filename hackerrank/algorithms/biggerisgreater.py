#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
def biggerIsGreater(w):
    alphabets = list(w)
    alphabets_copy = alphabets.copy()
    for i in range(-2,-len(alphabets)-1, -1):
        if alphabets[i] < alphabets[i+1]:
            for j in range(-1,i,-1):
                if alphabets[i] < alphabets[j]:
                    alphabets[i], alphabets[j] = alphabets[j], alphabets[i]
                    break
            alphabets[i+1:] = sorted(alphabets[i+1:])
            break
    if alphabets_copy == alphabets:
        return "no answer"
    else:
        return ''.join(alphabets)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
