#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2015-02-06
@summary:  https://www.codeeval.com/open_challenges/21/
'''
import sys
fileinput = open(sys.argv[1], 'r')
#fileinput = open('input.txt', 'r')

for test in fileinput:
    total = 0
    for i in test.strip():
        total += int(i)
    print total

fileinput.close()
