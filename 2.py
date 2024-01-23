#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
   
for i in range(4):
    for j in range(4):
        hourglass = [
            arr[i][j: j+3],
            [arr[i+1][j:j+1]],
            arr[i+2][j:j+3]
        ]
        currentSum = sum(sum(row) for row in hourglass)
        maxSum = max(maxSum, currentSum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
