#!/bin/python3

import math
import os
import random
import re
import sys

def palindrome(stri, low, high):

    while low < high:
        if stri[low] != stri[high]:
            return False

        low +=1
        high -=1

    return True

def palindromeIndex(stri):

    low = 0
    high = len(stri)-1

    while low < high:

        if stri[low] == stri[high]:
            low +=1
            high -= 1

        else:
            if palindrome(stri, low+1, high):
                return low
            if palindrome(stri, low, high-1):
                return high

            return 1

    return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        
        if result == -1:
            print("Palindrome")
        elif result == 1:
            print("No es posible")
        else:
            print(result)

        fptr.write(str(result) + '\n')

    fptr.close()
