#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-28
@summary:  Detects duplicate values in an array
https://www.codeeval.com/open_challenges/41/
'''
import sys, csv
fileinput = open(sys.argv[1], 'rb')
#fileinput = open('input.txt', 'rb')

csv_input = csv.reader(fileinput, delimiter=',')


for line in csv_input:
    ls = line[1:] # dont need the length of array
    ls.append(str.split(line[0], ';')[1])
    # counting sort idea
    count = dict()
    for k in ls:
        if str(k) in count.keys():
            print k
            break
        count[str(k)] = 1

fileinput.close()
