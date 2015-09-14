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
    array = [0] * s # O(n)

    for num in n_list: # O(n)
        rem = s-num
        if array[num] or array[rem]:
            return True
        array[rem] = 1
    return False

assert not sum_to([1, 3, 2, 5], 10)
assert sum_to([1, 3, 2, 5], 7)



if __name__ == '__main__':
    pass
