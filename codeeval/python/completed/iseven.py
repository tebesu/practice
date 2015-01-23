#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-27
@summary:  Codeeval, checks if a number is even. 1 for even, 0 false
'''



import sys
f = open(sys.argv[1], 'r')
for i in f:
    if int(i) % 2 == 0:
        print '1'
    else:
        print '0'
