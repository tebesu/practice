#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-09-14
@summary:
'''

def sum_to(n_list, s):
    '''
    Given a list of n numbers, find if any two numbers sum to s in O(n)
    Total time is: O(2n) ~ O(n)
    '''
    table = dict()

    for num in n_list: # O(n)
        if num < s:
            table[num] = s - num

    for key in table.keys(): # O(n)
        # Checking key should be O(1) depends on implementation
        if table[key] in table: # Check if remainder in table?
            return key, table[key]
    return False

import numpy as np
# np.random.seed(0)
high = 50
n = 10
a = np.random.randint(0, n, 2).ravel()
x = np.random.randint(0, high, n).ravel()

ans = x[a[0]] + x[a[1]]
print
print x
print ans
print sum_to(x, ans)



if __name__ == '__main__':
    pass
