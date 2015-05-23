#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-05-23
@summary:  Checks for duplicate strings
'''
# pylint: disable=all

def contains_dup(doc):
    '''
    Assume 128 chars
    '''
    duplicate = [False] * 128
    for char in doc:
        if duplicate[ord(char)]:
            return True
        duplicate[ord(char)] = True
    return False



if __name__ == '__main__':
    doc = 'abcdefhijklmnopqrstuv'
    assert not contains_dup(doc), 'Contains duplicate'

    doc += 'a'
    assert contains_dup(doc), 'Contains duplicate'

    doc += '1231'
    assert contains_dup(doc), 'Contains duplicate'
