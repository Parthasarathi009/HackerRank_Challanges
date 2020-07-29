#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump =0
    i=0
    while i < len(c)-2:
        if c[i]==0:
            if (c[i]==c[i+1]):
                jump+=1
                i+=1
                
                if (c[i+1]== c[i+2]):
                    i+=1
            
            else:
                i+=1
                jump+=1
        else:
            i+=1

    return jump
    #return len([x for x in c if x==0])-1
    #return len(list(filter( lambda x:(x == '0'), c)))-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
