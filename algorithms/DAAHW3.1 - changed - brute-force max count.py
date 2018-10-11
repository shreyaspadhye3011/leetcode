# Problem: input: an unsorted array A[lo..hi]; | output: a value that appears most often in the given subarray (ties are broken arbitrarily).
# Source: SCU COEN279 DAA HW3 Q1
# Author: Shreyas Padhye
# Algorithm: Brute Force (given in question). Check all possible cases

def brute_force_max_count(A):
    '''For an unsorted array, this function returns a value that appears most often in the array. In case of ties, it returns the leftmost element from A which has the max count'''
    assert (type(A) == list), 'Function expects the first parameter to be of list type'
    assert (len(A) > 0), 'Function expects A[] to be non-empty list'
    maxItem = None
    maxCount = 0
    for outerIndex in range(0, len(A) - 1):
        currCount = 0
        for innerIndex in range(outerIndex + 1, len(A)):
            if A[outerIndex] == A[innerIndex]:
                currCount += 1
        if (currCount > maxCount):
            maxItem = A[outerIndex]
            maxCount = currCount
    return maxItem

brute_force_max_count([1, 2, 3, 4, 2, 3, 3])    #3
# brute_force_max_count([1, 2, 3, 4, 2, 1, 1])  #1
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3])  #1
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3])  #1
# brute_force_max_count([1, 2, 3, 4, 2, 1, 2])  #2
