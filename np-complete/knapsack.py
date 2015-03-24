#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-03-24
@summary:  Knapsack Problem

Knapsack: B[k, w] = B[k-1, w],                                     if weight_k > w
                    max(B[k-1, w], B[k-1, w- weight_k] + value_k), otherwise
'''
# pylint: disable=C0103
import numpy as np
value_weights = [
    # Values, Weights
    (10, 5),
    (40, 4),
    (30, 6),
    (50, 3)
]

values, weights = zip(*value_weights)

max_weight = 10

B = np.zeros((len(values), max_weight+1))
keep = np.zeros((len(values), max_weight+1))

for k in xrange(len(values)):
    for w in xrange(max_weight+1):
        if weights[k] > w:
            # Element is too big, use prev row
            B[k, w] = B[k-1, w]
        else:
            # Prev element or prev element + value, considering weight
            if B[k-1, w] > B[k-1, w - weights[k]] + values[k]:
                B[k, w] = B[k-1, w]
            else:
                B[k, w] = B[k-1, w - weights[k]] + values[k]
                keep[k, w] = 1

# Obtain our solution
solution = []
K = max_weight
for i in xrange(len(keep)-1, 0, -1):
    if keep[i, K] == 1:
        K -= weights[i]
        solution.append((values[i], weights[i]))

spacing = max(max(zip(*solution)[0]), max(zip(*solution)[1])) / 10 + 1

print
print 'Solution: %s' % B[-1, -1]
print
# Print our dynamic programming table
print B
print
print 'Value {0} Weight'.format(' ' * spacing)
print '-' * (14 + spacing)

# Print solution
for v, w in solution:
    print '{0}{1}'.format(str(v) + (' ' * (spacing - len(str(v)) + 9)),
                          str(w) + (' ' * (spacing - len(str(w)))))

if __name__ == '__main__':
    pass
