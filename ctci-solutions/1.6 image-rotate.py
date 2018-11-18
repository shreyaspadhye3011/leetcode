# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

class solution():
    def rotate_image(self, M):
        # retrieve order of matrix
        n = len(M)     
        m = n          # considered n x n square, as given in question

        # initialize resultant matrix with 0
        R = [[0 for x in range(m)] for y in range(n)]

        # create 90 degree rotation
        for row in range(0, n):
            for col in range(0, n):
                R[col][n - row - 1] = M[row][col]
        return R

    def rotate_in_place(self, matrix):
        n = len(matrix)
        for layer in range(0, n/2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                offset = i - first
                top = matrix[first][i] # save top

                # left -> top
                matrix[first][i] = matrix[last-offset][first]
                
                # bottom -> left
                matrix[last-offset][first] = matrix[last][last - offset]
                
                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # top -> right
                matrix[i][last] = top # right <- saved top
        return matrix
    
t = solution()
# t.rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t.rotate_in_place([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# t.rotate_image([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
t.rotate_in_place([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
