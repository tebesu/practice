#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-28
@summary:  Detects duplicate values in an array
https://www.codeeval.com/open_challenges/41/
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-20
@summary:  Array duplicate numbers
https://www.codeeval.com/open_challenges/41/
'''
import sys
with open(sys.argv[1], 'r') as f:
#with open('input.txt', 'r') as f:
    for line in f:
        count = []
        numbers = line.strip().split(';')[-1].split(',')
        # counting sort idea
        for k in numbers:
            if k in count:
                print k
                break
            count.append(k)
