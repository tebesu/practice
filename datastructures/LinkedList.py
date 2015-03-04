#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-03-04
@summary:  Simple unordered linked list, very basic
           Could use a lot of improvement
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

class LinkedList(object):
    '''
    Simple linked list with many assumptions
    Lacks checking for a lot of cases
    Could be optimized with using tail better
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next_node = node
        self.tail = node
        self.count += 1

    def remove(self, item):
        # assume we have the element
        temp = self.head
        prev = self.head
        while temp != None:
            if temp.data == item:
                if prev == None:
                    self.head = temp.next_node
                else:
                    prev.next_node = temp.next_node
                break
            prev = temp
            temp = temp.next_node
        self.count -= 1

        if self.is_empty():
            self.tail = None
            self.head = None

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def search(self, item):
        cur = self.head
        while cur != None:
            if item == cur.get_data():
                return True
            cur = cur.next_node
        return False


    def append(self, item):
        node = Node(item)
        self.tail.next_node = node
        self.tail = node
        self.count += 1

    def insert(self, pos, item):
        node = Node(item)
        idx = 0
        cur = self.head
        while cur != None:
            if idx == (pos-1):
                node.next_node = cur.next_node
                cur.next_node = node
            cur = cur.next_node
            idx += 1
        self.count += 1

    def pop(self, pos=None):
        if pos == None:
            pos = self.count - 1
            idx = 0
        cur = self.head
        prev = cur
        while cur != None:
            if idx == pos:
                prev.next_node = cur.next_node
                if idx == (self.count - 1):
                    self.tail = prev
                    return cur

            prev = cur
            cur = cur.next_node
            idx += 1
        self.count -= 1
        return None

    def index(self, item):
        idx = 0
        cur = self.head
        while cur != None:
            if item == cur.get_data():
                return idx
            cur = cur.next_node
            idx += 1
        return -1

    def __str__(self):
        s = ''
        cur = self.head
        while cur != None:
            s += '--> [%s]' % cur.get_data()
            cur = cur.next_node
        return s


if __name__ == '__main__':
    ls = LinkedList()
    ls.add(5)
    ls.add(3)
    ls.add(10)
    print ls

    ls.insert(1, 20)
    print ls
    print ls.index(20)
