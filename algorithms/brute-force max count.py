# Problem: input: an unsorted array A[lo..hi]; | output: a value that appears most often in the given subarray (ties are broken arbitrarily).
# Source: SCU COEN279 DAA HW3
# Author: Shreyas Padhye
# Algorithm: Brute Force (given in question). Check all possible cases

def brute_force_max_count(A, S):
    '''For an unsorted array, this function returns a value that appears most often in a given subarray. In case of ties, it returns the leftmost element from S which has the max count'''
    # TODO: handle edge cases like A has 0 elements or B has 0 elements or some other type than k=list is passed. Use assert if needed
    # TODO: check case when nothing in S exists in A, what happens then? should return None
    maxItem = A[0]
    maxCount = 0
    for currItem in S:
        currCount = 0
        for index in range(0, len(A)):
            if A[index] == currItem:
                currCount += 1
        print('Count of ', currItem, ' is: ', currCount)
        if (currCount > maxCount):
            maxItem = currItem
            maxCount = currCount
    
    if maxCount > 0:   # case when no element from S[] is found in A[]
        return maxItem
    else:
        return None

brute_force_max_count([1, 2, 3, 4, 2, 1, 1], [1, 2])
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3], [1, 8, 2])
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3], [7, 8, 5])
