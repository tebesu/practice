#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-27
@summary:  Inputs space delimited characters followed by an int. Print the mth to the last element.
https://www.codeeval.com/open_challenges/10/
'''
import sys

with open(sys.argv[1], 'r') as f:
#with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip().split(' ')
        # Last element is the int specifying m
        m = int(line[-1])
        # If index is within range, print it
        if len(line) > m:
            print line[-m-1]
