#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from collections import defaultdict
#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    m = len(topic[0])
    idx = list(range(1, len(topic) + 1))
    teams = combinations(idx, 2)
    d = defaultdict(lambda: 0)
    for team in teams:
        subject = bin(int(topic[team[0] - 1], 2) | int(topic[team[1] - 1], 2))[2:]
        subject = subject.zfill(m)
        d[subject.count("1")] += 1
    return [max(d.keys()), d[max(d.keys())]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
