#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-06-08
@summary:
https://www.codeeval.com/open_challenges/34/
'''
import sys






def find_pairs(A, target):
    '''
    Given a sorted list of numbers it returns a list of tuples that sum to that
    number. No repeats, no negative numbers, no sum same number
    '''
    # Bounds check
    if A[-1] + A[-2] < target:
        return None

    results = list()
    # Iterate reverse
    for i in xrange(len(numbers)-1, 0, -1):
        # Bounds check
        if A[i] > target:
            continue

        j = i-1
        while j >= 0:
            if A[j] + A[i] > target:
                j -= 1
            elif A[j] + A[i] == target:
                results.append((A[j], A[i]))
                j -= 1
            else:
                break

    if len(results) == 0:
        return None

    return results




with open(sys.argv[1], 'r') as f:
    for line in f:
        numbers, target = line.split(';')
        target = int(target)
        numbers = [int(number) for number in numbers.split(',')]

        results = find_pairs(numbers, target)

        if results is None:
            print 'NULL'
        else:
            print ';'.join(['{0},{1}'.format(a, b) for a, b in results])



if __name__ == '__main__':
    pass
