#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-20
@summary:  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
https://projecteuler.net/problem=6
'''

def sum_of_squares(n):
    '''
    sum of squares = \sum\limits_{i=1}^{n} i^2
    closed form = (n (n+1) (2n+1)) / 6

    returns sum of 1^2 + 2^2 + ... + n^2
    '''
    return (n * (n + 1) * (2 * n + 1)) / 6


def sum_of_series(n):
    '''
    Sum of a series = \sum\limits_{i=1}^n i
    closed form = n(n+1) / 2

    returns: sum of 1 + 2 + 3 + ... + n
    '''
    return (n * (n + 1)) / 2

n = 100
sum_squares = sum_of_squares(n)
square_of_sum = sum_of_series(n) ** 2

print square_of_sum - sum_squares


if __name__ == '__main__':
    pass
