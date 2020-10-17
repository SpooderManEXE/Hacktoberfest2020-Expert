#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diag1 = 0
    elem1 = 0
    elem2 = len(arr[1])-1
    diag2 = 0
    final_sum = 0
    
    for i in arr:
        
        diag1 += i[elem1]
        diag2 += i[elem2]
        print(diag1,diag2)
        elem2 -= 1
        elem1 += 1
        if(elem1 == len(i)):
            final_sum = abs(diag1 - diag2) 
            print(final_sum)
            return(final_sum)
            break
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
