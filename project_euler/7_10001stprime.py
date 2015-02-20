#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-20
@summary:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

primes = [2]
# we only check odd numbers
for i in xrange(3, int(1e6), 2):
    is_prime = True

    # we only need to check up to sqrt(i) for its prime
    for j in xrange(2, int(i ** 0.5) + 1):
        if i % j is 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)
        if len(primes) == 10001:
            break

print primes[-1]
