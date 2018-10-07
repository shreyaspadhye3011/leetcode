# Problem: input: an unsorted array A[lo..hi]; | output: a value that appears most often in the given subarray (ties are broken arbitrarily).
# Source: SCU COEN279 DAA HW3 Q1
# Author: Shreyas Padhye
# Algorithm: Transform-Conquer. Sort and check immediate right neighbour as you pass through the array. When neighbour's not a duplicate, update checkItem to current instance

def brute_force_max_count(A, S):
    '''For an unsorted array, this function returns a value that appears most often in a given subarray. In case of ties, it returns the leftmost element from S which has the max count'''
    maxItem = A[0]
    maxCount = 0
    
    
    if maxCount > 0:   # case when no element from S[] is found in A[]
        return maxItem
    else:
        return None

brute_force_max_count([1, 2, 3, 4, 2, 1, 1], [1, 2])
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3], [1, 8, 2])
# brute_force_max_count([1, 2, 3, 4, 2, 1, 3], [7, 8, 5])
