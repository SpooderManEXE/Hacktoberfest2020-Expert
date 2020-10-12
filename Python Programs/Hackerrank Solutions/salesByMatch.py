#!/bin/python3

import math
import os
import random
import re
import math
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # print(ar)
    count=0
    dic={}
    for i in ar:
        if(i in dic.keys()):
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic.keys():
        
        if(dic[i]%2==0):
            num=dic[i]/2
            count+=int(num)
        elif(dic[i]>1):
            rem=math.floor(dic[i]/2)
            print(rem,dic[i])
            count+=rem
                                                        
    return(count) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
