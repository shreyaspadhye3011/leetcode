# Problem: input: an unsorted array A[lo..hi]; | output: the (left) median of the given array
# Source: SCU COEN279 DAA HW3 Q3
# Author: Shreyas Padhye
# Algorithm: Decrease-Conquer

def left_median(A):
    if len(A) == 1 or len(A) == 2:
        return A[0]
    else:
        return merge