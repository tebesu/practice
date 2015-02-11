#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-27
@summary:  Codeeval, checks if a number is even. 1 for even, 0 false
https://www.codeeval.com/open_challenges/100/
'''
import sys
f = open(sys.argv[1], 'r')
# 18 ms improvement
for i in f:
    print 1 if int(i) % 2 == 0 else 0
