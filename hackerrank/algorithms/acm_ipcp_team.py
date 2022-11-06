#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    teams = list(combinations(topic, 2))
    m_team = 0
    m_topics = 0
    cur_team = 1
    for p1, p2 in teams:
        t = 0
        for i in range(len(topic[0])):
            if p1[i] == '1' or p2[i] == '1':
                t += 1
        if t > m_topics:
            m_topics = t
            m_team = cur_team
        cur_team += 1
    return([m_topics, m_team])

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
