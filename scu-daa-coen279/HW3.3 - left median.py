# Problem: input: an unsorted array A[lo..hi]; | output: the (left) median of the given array
# Source: SCU COEN279 DAA HW3 Q3
# Author: Shreyas Padhye
# Algorithm: Decrease-Conquer

class solution():
    def left_median(self, A):
        if len(A) == 1 or len(A) == 2:
            return A[0]
        else:
            median = self.left_median(A[:-1])
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
                med_neighbour = A.index(median) - 1
                if A[-1] > A[med_neighbour]:
                    temp = A[-1]
                    A[-1] = A[med_neighbour]
                    A[med_neighbour] = temp
                return A[med_neighbour]

t = solution()
# t.left_median([0, 1, 3, 5])   #1
# t.left_median([0, 1, 3, 5, 2])   #2
# t.left_median([0, 1, 3, 5])   #1
t.left_median([0, 1, 3, 5])   #1
t.left_median([5, 1, 3, 8, 2])   #5
t.left_median([7, 0, 1, 12, 1, 45, 2])   #7
t.left_median([7, 0, 1, 12, 45, 2, 11, 8, 101, 14])   #correct: 8, mine: 12
# t.left_median([7, 0, 1, 12, 1, 45, 2, 11, 8, 101, 14])   #correct: 8, mine: 1
