# Reference: https://leetcode.com/problems/number-of-islands/

class Solution(object):
    islandCount = 0
    visited_dict = {}
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rowLen = len(grid)
        colLen = len(grid[0])       # considering symmetric matrix. Also add defensive condition on index 0 access
        self.recurseNumIslands(self, grid, 0, 0, rowLen, colLen, False)
        return self.islandCount

    def recurseNumIslands(self, grid, row, col, rowLen, colLen, continuation):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # rowLen = len(grid)
        # for row in range(rowLen):
        #     colLen = len(grid[row])
        #     for col in range(colLen):
        if (row, col) not in self.visited_dict:
            self.visited_dict[(row, col)] = 'visited'
            if grid[row][col] == 1 and continuation == False:
                self.islandCount += 1
                continuation = True
            
            elif grid[row][col] == 0:
                continuation = False

            # todo: call neighbors recursively with their respective value of continuation
            if row + 1 < rowLen:
                self.recurseNumIslands(grid, row + 1, col, rowLen, colLen, continuation)
            if col + 1 < colLen:
                self.recurseNumIslands(grid, row, col + 1, rowLen, colLen, continuation)

        # print(self.visited_dict)      
    
obj = Solution()
obj.numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])
