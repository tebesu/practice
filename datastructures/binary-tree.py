#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-02-22
@summary:
'''
# pylint: disable=all

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return '{0}'.format(self.key)

    def __repr__(self):
        return 'Key: {0:<5}\tParent: {1:<5}\tLeft: {2:<5}\tRight: {3:<5}'.format(self.key,
                                                                     self.parent,
                                                                     self.left,
                                                                     self.right)
def _search(node, key):
    '''
    Searches the binary tree for a key
    Directs it left if smaller and right if bigger

    Iterative is faster than recursive
    '''
    temp = node
    prev = temp
    while temp != None or temp != None and key != temp.key:
        if key < temp.key:
            prev = temp
            temp = temp.left
        else:
            prev = temp
            temp = temp.right

    return prev


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.length

    @property
    def length(self):
        return self.size

    def max(self, node=None):
        '''
        Returns the maximum value in the tree
        '''
        temp = self.root if node == None else node
        while temp.right != None:
            temp = temp.right
        return temp

    def min(self, node=None):
        '''
        Returns the min value in the tree
        '''
        temp = self.root if node == None else node
        while temp.left != None:
            temp = temp.left

        return temp

    def __transplant(self, u, v):
        # Replace U with V

        # u is the root
        if u.parent == None:
            self.root = v

        # u is a left child
        elif u.key == u.parent.left.key:
            u.parent.left = v

        # u is a right child
        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent


    def __delete_node(self, node):
        '''
        Deletes a node
        '''
        # No left element
        if node.left == None:
            self.__transplant(node, node.right)

        # No right element
        elif node.right == None:
            self.__transplant(node, node.left)
        else:
            temp = self.min(node)

            if temp.parent != node:
                self.__transplant(temp, temp.right)
                temp.right = node.right
                temp.right.parent = temp

            self.__transplant(node, temp)
            temp.left = node.left
            temp.left.parent = node

    def delete(self, key):
        '''
        Deletes a node given a key
        '''
        node = self.search(key)
        if node != None:
            self.__delete_node(node)
            self.size -= 1
        else:
            raise KeyError('No such node exists in tree')

    def insert(self, key):
        '''
        Inserts a node, left if key < parent else right
        Left has smaller, right has bigger
        '''
        self.size += 1
        node = Node(key)
        cur = None
        parent = self.root
        while parent is not None:
            cur = parent
            parent = parent.left if node.key < parent.key else parent.right
        node.parent = cur
        if cur is None:
            self.root = node
        elif node.key < cur.key:
            cur.left = node
        else:
            cur.right = node

    def search(self, key):
        '''
        Searches for a given element in the tree
        '''
        return _search(self.root, key)

    def __inorder_tree_walk(self, node):
        '''
        prints out the elements in order
        '''
        if node != None:
            self.__inorder_tree_walk(node.left)
            print node.key
            self.__inorder_tree_walk(node.right)


    def __str__(self):
        '''
        Prints the tree out by depth
        '''
        s = dict()
        depth = 0
        def recursive(node, depth):
            if node != None:
                recursive(node.left, depth + 1)
                temp = s.get(depth, None)
                if temp:
                    temp.append(node.key)
                else:
                    temp = [node.key]
                s[depth] = temp
                recursive(node.right, depth + 1)
        recursive(self.root, 1)
        output = []
        for depth in sorted(s.keys()):
            layer = ''
            for v in s[depth]:
                layer += '{0}{1}'.format(' ' * depth, v)
            output.append(layer)
        return '\n'.join(output)


    def print_tree(self):
        self.__inorder_tree_walk(self.root)

if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(3)
    bt.insert(20)
    bt.delete(5)
    print
    print bt
