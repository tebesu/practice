#!/usr/bin/env python
'''
@author:   Travis A. Ebesu
@created:  2014-07-18
@summary:  Code Eval: Prints odd numbers
https://www.codeeval.com/open_challenges/25/
'''

# 5.26ms
print '\n'.join([str(i) for i in xrange(1, 100, 2)])
# 5.49ms
# for i in xrange(1, 100, 2):
#     print i
