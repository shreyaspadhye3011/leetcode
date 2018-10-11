# Problem: input: an unsorted array A[lo..hi]; | output: a value that appears most often in the array (ties are broken arbitrarily).
# Source: SCU COEN279 DAA HW3 Q2
# Author: Shreyas Padhye
# Algorithm: Transform-Conquer. Sort and check immediate right neighbour as you pass through the array. When neighbour's not a duplicate, update checkItem to current instance. 

def transform_conquer_max_count(A):
    '''For an unsorted array, this function returns a value that appears most often in the given array. In case of ties, it returns the leftmost element from the array which has the max count'''
    assert (type(A) == list), 'Function expects the first parameter to be of list type'
    assert (len(A) > 0), 'Function expects A[] to be non-empty list'
    
    # sort the array as a transformation step
    A.sort()
    currItem = A[0]
    currCount = 1
    maxItem = A[0]
    maxCount = 1
    
    # pass through the array and keep track of repititions
    for item in A:
        if item == currItem:
            currCount += 1
        else:
            if currCount > maxCount:
                maxItem = currItem
                maxCount = currCount
            currItem = item
            currCount = 1

    return maxItem

transform_conquer_max_count([1, 2, 3, 4, 2, 1, 1])      #1
# transform_conquer_max_count([1, 2, 3, 4, 2, 3, 3])    #3
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 1])    #1
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 3])    #1
# transform_conquer_max_count([6, 7, 8, 9])             #6
