#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # page number
    page = 0
    # total specical problem
    special_problem_count = 0

    for i in range(n):
        # each chapter has arr[i] problems and each chapter start from 1
        problem_set_num = 0

        # find the problem set number in each page per chapter
        while arr[i] > 0:
            # update the page number
            page += 1
            # print("chapter= ", i, "total problem set= ", arr[i], "problemset= ", problem_set_num, "page= ", page)

            # check if remain problem set is less than k
            start = problem_set_num
            if arr[i] <= k:
                # update the problem set number
                problem_set_num += arr[i]
                # check if problem set number is in the page
                if start < page and page <= problem_set_num:
                    # update the special problem count
                    special_problem_count += 1
            else:
                # update the problem set number
                problem_set_num += k
                if start < page and page <= problem_set_num:
                    # update the special problem count
                    special_problem_count += 1

            # update the remain problem set
            arr[i] -= k
            # print(">> chapter= ", i, "remain problem set= ", arr[i], "problemset= ", problem_set_num, "page= ", page,
            #       "special = ", special_problem_count)

    # return total special problem
    return special_problem_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
