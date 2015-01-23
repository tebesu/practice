#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-27
@summary:  Inputs space delimited characters followed by an int. Print the mth to the last element.
https://www.codeeval.com/open_challenges/10/
'''
import sys, csv
#fileinput = open(sys.argv[1], 'rb')
fileinput = open('input.txt', 'rb')

csv_input = csv.reader(fileinput, delimiter=' ')

for line in csv_input:
    # Last element is the int specifying m
    m = int(line[-1])
    # If index is within range, print it
    if len(line) > m:
        print line[-m-1]

    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

fileinput.close()
