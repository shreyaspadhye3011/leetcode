# Reference: CTCI. Pg 48
# Author: Shreyas Padhye

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column is set to 0.

# Algorithm: Keep track of the indices to be zeroed by a single pass. Do another iteration over the matrix and change to 0 as per the stored list

class solution():
    def matrix_zero_extra_space(self, M):
        # retrieve order of matrix
        n = len(M)
        zeroes = []
        for i in range(n):
            for j in range(n):
                if M[i][j] == 0:
                    zeroes.append(i)
                    zeroes.append(j)
        zero_set = list(set(zeroes))        # as unique entries of indices required

        # Algo - for every position check if needs to be zeroed
        # for i in range(n):
        #     for j in range(n):
        #         if i in zero_set or j in zero_set:
        #             M[i][j] = 0
        
        # Algo - for every index in the zero_set, set the row and col to zero together
        for index in zero_set:
            for i in range(n):
                M[index][i] = 0
                M[i][index] = 0

        return M

t = solution()
t.matrix_zero_extra_space([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t.matrix_zero_extra_space([[0, 2, 3], [4, 5, 6], [7, 8, 9]])
t.matrix_zero_extra_space([[0, 2, 3], [4, 5, 6], [7, 8, 0]])
t.matrix_zero_extra_space([[0, 2, 3, 1], [4, 0, 6, 7], [7, 8, 0, 1], [3, 6, 7, 8]])
t.matrix_zero_extra_space([[3, 2, 3, 1], [4, 0, 6, 7], [7, 8, 1, 1], [3, 6, 7, 8]])