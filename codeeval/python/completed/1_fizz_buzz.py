#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-20
@summary:  Fizz Buzz divisibility tests
https://www.codeeval.com/open_challenges/1/
'''
import sys

with open(sys.argv[1], 'r') as f:
#with open('input.txt', 'r') as f:
    for line in f:
        x, y, n = [int(x) for x in line.strip().split(' ')]
        ls = list()
        for i in xrange(1, n+1):
            if i % y == 0 and i % x == 0:
                ls.append('FB')
            elif i % x == 0:
                ls.append('F')
            elif i % y == 0:
                ls.append('B')
            else:
                ls.append(str(i))
        print ' '.join(ls)
