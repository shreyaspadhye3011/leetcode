# Reference: https://leetcode.com/problems/number-of-islands/

class Solution(object):
    islandCount = 0
    continuation = False
    visited_dict = {}
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                print(row, col)
                
    
obj = Solution()
obj.numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])
