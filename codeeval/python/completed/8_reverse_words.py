#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-22
@summary:  Reverse words

https://www.codeeval.com/open_challenge_scores/?pkbid=8
'''
import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        # Slice starting from last element, increment by -1
        print ' '.join(line.strip().split()[-1::-1])
