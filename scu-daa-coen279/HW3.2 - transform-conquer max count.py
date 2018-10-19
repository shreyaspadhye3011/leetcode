# Problem: input: an unsorted array A[lo..hi]; | output: a value that appears most often in the given subarray (ties are broken arbitrarily).
# Source: SCU COEN279 DAA HW3 Q1
# Author: Shreyas Padhye
# Algorithm: Transform-Conquer. Sort and check immediate right neighbour as you pass through the array. When neighbour's not a duplicate, update checkItem to current instance. 
# 
# Map in single pass: Store iteration count of all elements in dictionary. Finally, do a single pass over S to find maxCount within the elements that are under consideration 

def transform_conquer_max_count(A, S):
    '''For an unsorted array, this function returns a value that appears most often in a given subarray. In case of ties, it returns the leftmost element from S which has the max count'''
    assert (type(A) == list), 'Function expects the first parameter to be of list type'
    assert (len(A) > 0), 'Function expects A[] to be non-empty list'

    maxItem = None
    maxCount = 0
    countDictionary = {}
    
    # create a dictionary to keep track of iteration of every element
    for item in A:
        if item in countDictionary:
            countDictionary[item] += 1
        else:
            countDictionary[item] = 1
    
    # print(countDictionary)
    
    # do a single pass over the sub array, S to find maxCount within the set of elements that are under consideration
    for checkItem in S:
        if checkItem in countDictionary:
            if countDictionary[checkItem] > maxCount:
                maxItem = checkItem
                maxCount = countDictionary[checkItem]
    return maxItem

transform_conquer_max_count([1, 2, 3, 4, 2, 1, 1], [1, 2])      #1
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 3], [7, 8, 5]) #None
# transform_conquer_max_count([1, 2, 3, 4, 2, 3, 3], [2, 3, 1]) #3
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 1], [1, 2])    #1
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 3], [1, 8, 2]) #1
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 2], 23)        #assertion error 
# transform_conquer_max_count([1, 2, 3, 4, 2, 1, 2], ['as', 4]) #4
