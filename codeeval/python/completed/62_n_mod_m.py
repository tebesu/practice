#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-20
@summary:  n mod m without modulo operator
https://www.codeeval.com/open_challenges/62
'''
import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        n, m = [float(x) for x in line.split(',')]
        # remainder * m = mod
        nmodm = ((n / m) - (n // m)) * m
        print '{0:.0f}'.format(nmodm)
