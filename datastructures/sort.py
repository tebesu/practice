#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2015-03-19
@summary:
'''
# pylint: disable=C0103, W0621
from random import randint, seed

def swap(ls, i, j):
    '''
    Swaps two elements in a list-like object
    NOTE: Inplace

    Parameters
    ----------
    ls : list
        list to swap elements
    i : int
        position one to switch with position two
    j : int
        position two to switch with position one

    '''
    ls[i], ls[j] = ls[j], ls[i]


def partition(A, low, high):
    '''
    Partition function for quicksort, takes a pivot as the last element.
    elements <= pivot > elements

    Parameters
    ----------
    A : array
        Array to sort
    low : int
        The low index of the array
    high : int
        The high index of array

    Returns
    -------
    idx : int
        The index of the pivot
    '''
    idx = low
    x = A[high]
    for j in xrange(low, high):
        if A[j] <= x:
            swap(A, idx, j)
            idx += 1

    # Fix the last element
    swap(A, idx, high)
    return idx

def random_partition(A, low, high):
    '''
    Swaps the randomized element with last element.
    Partition always uses last element as pivot.
    '''
    pivot = randint(low, high)
    swap(A, pivot, high)
    return partition(A, low, high)

def random_quicksort(A, low, high):
    '''
    Randomsized quicksort, calls random partition instead
    '''
    if low < high:
        x = A[high]
        pivot = random_partition(A, low, high)
        quicksort(A, low, pivot-1)
        quicksort(A, pivot+1, high)

def median_quicksort(A, low, high):
    '''
    quicksort using median as pivot
    '''
    if low < high:
        x = quickselect(A, low, high, (high-low+1) / 2) # Get median
        swap(A, x, high)
        pivot = partition(A, low, high)
        median_quicksort(A, low, pivot-1)
        median_quicksort(A, pivot+1, high)

def quicksort(A, low, high):
    '''
    Quicksort
    Runtime:   O(n lg n) (expected)
    Stable:    Yes
    In-Place:  No (but can be implemented)
    '''
    if low < high:
        pivot = partition(A, low, high)
        quicksort(A, low, pivot-1)
        quicksort(A, pivot+1, high)

def merge(a, b):
    '''
    Takes two arrays and sort merges them together
    Expects: deques
    '''
    c = []
    i, j = 0, 0
    while j < len(a) and i < len(b):
        if a[j] > b[i]:
            c.append(b[i])
            i += 1
        else:
            c.append(a[j])
            j += 1

    while j < len(a):
        c.append(a[j])
        j += 1

    while i < len(b):
        c.append(b[i])
        i += 1
    return c

def mergesort(A):
    '''
    Mergesort: splits an array sorts then merges them together
    Runtime:   O(n lg n)
    Stable:    Yes
    In-Place:  No
    '''
    if len(A) == 1:
        return A
    mid = len(A) / 2
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])
    return merge(left, right)
#    return merge(deque(left), deque(right))

def quickselect(A, p, r, i):
    '''
    ith order statistic
    '''
    if p == r:
        return p+1
    q = random_partition(A, p, r)
    k = q - p + 1
    if i == k: # check if correct element
        return p+k
    elif i < k:
        return quickselect(A, p, q-1, i) # low side
    else:
        return quickselect(A, q+1, r, i-k) # high sid, offset i relative to q+1

def insertion_sort(A):
    '''
    Insertion Sort
    Runtime:   O(n^2)
    Stable:    Yes
    In-Place:  Yes
    '''
    for i in xrange(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            swap(A, j, j-1)
            j -= 1

def is_sorted(A):
    '''
    Checks if an array is sorted
    '''
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False

    return True


def create_random_array(size, min_random, max_random, rand_seed=0):
    '''
    Creates a list of random elements of size specified and the minimum
    and maximum random integers

    Parameters
    ----------
    size : int
        size of array
    min_random : int
        minimum random integer
    max_random : int
        maximum random integer
    rand_seed : int
        random seed (optional)

    Returns
    -------
    array : list
        randomized array of elements
    '''
    seed(rand_seed)
    return [randint(min_random, max_random) for x in xrange(size)]



from pythonutils.parallel import Timer
timer = Timer()
minimum = -int(1e5)
maximum = int(1e5)
elements = int(1e5)
print


for i in range(10):
    A = create_random_array(elements, minimum, maximum)
    timer.start()
    #median_quicksort(A, 0, len(A)-1)
    #random_quicksort(A, 0, len(A)-1)
    #quicksort(A, 0, len(A)-1)
    #insertion_sort(A)
    A = mergesort(A)
    timer.stop()
    if not is_sorted(A):
        print 'ERROR: Not sorted'
        break
timer.print_cumulative()




'''
%%timeit -n 5 A = create_random_array(elements, minimum, maximum)
insertion_sort(A)

%%timeit -n 5 A = create_random_array(elements, minimum, maximum)
quicksort(A, 0, len(A)-1)

%%timeit -n 5 A = create_random_array(elements, minimum, maximum)
mergesort(A)
'''
if __name__ == '__main__':
    pass
