# Problem: input: an unsorted array A[lo..hi]; | output: the largest and smallest values M and m in A[lo..hi]
# Source: SCU COEN279 DAA HW3 Q4
# Author: Shreyas Padhye
# Algorithm: Divide and Conquer

def high_low_dnc(A):
    '''For an unsorted array, this function returns the [max, min] from the array'''
    n = len(A)
#     print(n)
    rearranged_list = []
    if n == 1:
        return [A[0]]
    
    # TODO: handle / test odd case
    # Divide step: call function recursively on two halves
    left = high_low_dnc(A[:int(n/2)])
    right = high_low_dnc(A[(int(n/2)):])
    left_index = 0
    right_index = 0

    # Merge step A: make decision which is max element
    if left[0] > right[0]:
        rearranged_list.append(left[0])
        left_index += 1
    else:
        rearranged_list.append(right[0])
        right_index += 1

    # Merge step B: make decision which half contains min
    # if last index of left is smaller than  right, insert right first
    # TODO: check whether there's a way of copying a list from a particular index "as is" into another list from a particular position. If not, create your own function and keep as util
    if left[-1] < right[-1]:
        while right_index < len(right):
            rearranged_list.append(right[right_index])
            right_index += 1
        while left_index < len(left):
            rearranged_list.append(left[left_index])
            left_index += 1
    else:
        while left_index < len(left):
            rearranged_list.append(left[left_index])
            left_index += 1
        while right_index < len(right):
            rearranged_list.append(right[right_index])
            right_index += 1

    # rearranged_list[0] & rearranged_list[-1] will have max & min elements respectively
    return [rearranged_list[0], rearranged_list[-1]]

high_low_dnc([13, 8, 2, 7, 41, 1, 7, 81])   #O: [81, 1]
# high_low_dnc([13, 8, 2, 7, 41, 79, 7, 6])   #O: [79, 2]
# high_low_dnc([101, 3, 7, 41, 79, 7, 6])   #O: [101, 3]
# high_low_dnc([7, 3, 1])   #O: [7, 1]
# high_low_dnc([7, 7, 1, 1])   #O: [7, 1]
# high_low_dnc([7, 7])   #O: [7, 7]