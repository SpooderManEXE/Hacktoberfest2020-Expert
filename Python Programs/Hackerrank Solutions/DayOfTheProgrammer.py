#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    result=""
    if(year>1918):
        if(year%400==0):
            #leap Year
            result="12.09."+str(year)
        elif(year%4==0):
            if(not year%100==0):
                #leap Year
                result="12.09."+str(year)
            else:
                result="13.09."+str(year)
        else:
            # normal Year
            result="13.09."+str(year)


    elif(year==1918):
        print("here")
        result= "26.09."+str(year)


    else:
        if(year%4==0):
                result="12.09."+str(year)
        else:
            # normal Year
            result="13.09."+str(year)


    return(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
