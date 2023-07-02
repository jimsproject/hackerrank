#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n -> changes to list of width
#  2. 2D_INTEGER_ARRAY cases
#


# there issues with the function, rather passing n , cases. it should passing width and cases
def serviceLane(width, cases):
    # desc get min servicelane width on given segment

    res = []
    for i in range(len(cases)):
        # get segment
        start = cases[i][0]
        end = cases[i][1]+1

        # get slices of width on given segment
        segment = width[start:end]
        # find minimum width and store in list res
        res.append(min(segment))

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)


    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
