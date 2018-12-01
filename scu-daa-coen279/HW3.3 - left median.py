# Problem: input: an unsorted array A[lo..hi]; | output: the (left) median of the given array
# Source: SCU COEN279 DAA HW3 Q3
# Author: Shreyas Padhye
# Algorithm: Decrease-Conquer

def left_median(A):
    if len(A) == 1 or len(A) == 2:
        return A[0]
    else:
        median = left_median(A[:-1])
        if len(A[:-1]) % 2 == 0:
            if median > A[-1]:
                return median
            else:
                med_neighbour = A.index(median) + 1
                if A[-1] < A[med_neighbour]:
                    temp = A[-1]
                    A[-1] = A[med_neighbour]
                    A[med_neighbour] = temp
                return A[med_neighbour]
        elif median < A[-1]:
            return median
        else:
        

        return