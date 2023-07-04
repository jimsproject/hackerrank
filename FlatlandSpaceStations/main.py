#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # sorting station order
    c.sort()
    # get distance from first city to first station and last city to last station
    max_distance = max(c[0], n-1 - c[-1])

    # check distance between each station
    for i in range(len(c) - 1):
        mid_city = (c[i] + c[i+1]) // 2  # city between 2 station
        distance = mid_city - c[i]  # the farthest distance is in the middle  distance 2 space station

        # compare with existing distance
        max_distance = max(max_distance, distance)

    return max_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
