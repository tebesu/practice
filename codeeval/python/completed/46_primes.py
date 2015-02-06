#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2015-2-6
@summary: https://www.codeeval.com/open_challenges/46/
          Finds all primes less than n
'''
import sys
from math import sqrt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s = ''
    if int(test) >= 2:
        s += '2'
    for i in range(3, int(test), 2):
        prime = True
        for j in range(3, int(sqrt(i))+1, 2):
            if i % j == 0:
                prime = False
        if prime:
            s += ',' + str(i)
    print s
test_cases.close()
