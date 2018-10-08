# Problem: input: an unsorted array A[lo..hi]; | output: a value that appears most often in the given subarray (ties are broken arbitrarily).
# Source: SCU COEN279 DAA HW3 Q1
# Author: Shreyas Padhye
# Algorithm: Brute Force (given in question). Check all possible cases

def brute_force_max_count(A, S):
    '''For an unsorted array, this function returns a value that appears most often in a given subarray. In case of ties, it returns the leftmost element from S which has the max count'''
    assert (type(A) == list and type(S) == list), 'Function expects both parameters to be non-empty lists'
    assert (len(A) > 0 and len(S) > 0), 'Both main array, A[] & sub array, S[] need to be non-empty'
    maxItem = None
    maxCount = 0
    for currItem in S:
        currCount = 0
        for index in range(0, len(A)):
            if A[index] == currItem:
                currCount += 1
        if (currCount > maxCount):
            maxItem = currItem
            maxCount = currCount
        return maxItem

brute_force_max_count([1, 2, 3, 4, 2, 3, 3], [2, 3, 1])    #3
# brute_force_max_count([1, 2, 3, 4, 2, 1, 1], [1, 2])    #1
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3], [1, 8, 2]) #1
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3], [7, 8, 5])   #None
# brute_force_max_count([1, 2, 3, 4, 2, 1, 2], 23)  #assertion error 
# brute_force_max_count([1, 2, 3, 4, 2, 1, 2], ['as', 4])  #4
