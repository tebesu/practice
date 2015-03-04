#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-24
@summary:  Exercises from problem solving with algorithms & data structures
           Note: these are my own implementations so they vary a bit from th sol
'''

class Stack(object):
    '''
    Simple stack implementation using a python list
    Lists allow for constant time for append/pop
    '''
    def __init__(self):
        self.items = []

    def push(self, item):
        '''
        Push an item to the top of stack
        '''
        self.items.append(item)

    def pop(self):
        '''
        Pop the last item on the stack
        '''
        return self.items.pop()

    def peek(self):
        '''
        Peek at the top item on the stack, dont remove it
        '''
        return self.items[-1]

    def is_empty(self):
        '''
        Returns true if the stack is empty
        '''
        return self.items == []

    def size(self):
        '''
        Returns the number of elements in the stack
        '''
        return len(self.items)


def par_checker(symbol_list):
    '''
    Uses a stack to check if parenthesis are properly nested
    '''
    stack = Stack()
    for symbol in symbol_list:
        if symbol in ['(', '{', '[']:
            stack.push(symbol)
        elif symbol in [')', '}', ']']:
            if match(stack.peek(), symbol):
                if stack.is_empty():
                    return False
                stack.pop()
            else:
                return False
    return stack.is_empty()

def match(stack_top, symbol):
    '''
    returns if the  opening and closing symbol match
    '''
    idx = ['(', '{', '['].index(stack_top)
    return [')', '}', ']'][idx] == symbol


def dec_to_binary(num):
    '''
    Converts a decimal base 10 number to binary
    '''
    return base_converter(num, 2)

def base_converter(num, base):
    '''
    Converts a base 10 to any other base to 16
    '''
    digits = "0123456789ABCDEF"
    stack = Stack()
    while num != 0:
        num, remain = divmod(num, base)
        stack.push(remain)
    return ''.join([str(digits[stack.pop()]) for x in range(stack.size())])

# dec = 500
# binary = dec_to_binary(dec)
# print '{0}\t==>\t{1}\tCorrect: {2}'.format(dec, binary,
#                                            int(binary, 2) == dec)
# print base_converter(25, 16)
# print oct(25), hex(25)


if __name__ == '__main__':
    # Check our paraenthesis
    assert par_checker('(((asdf)))') == True
    assert par_checker('(()') == False
    assert par_checker('{{([][])}()}') == True
    assert par_checker('[{()]') == False
