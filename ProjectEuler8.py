#!/bin/python

import sys

def findProd(num1):
    mult = 1
    
    for i in num1 :
        mult = mult * int(i)
    
    return mult


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input().strip()
    start = 0
    end = k
    
    mult = [1 for x in xrange(n-k)]
    num1 = list(str(num))
    
    for i in xrange(n-k) :
        mult[i] = findProd(num1[start:end])
        start = start +1
        end = end + 1
        
    print max(mult)