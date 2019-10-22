# Reference: https://leetcode.com/problems/number-of-islands/

class Solution(object):
    islandCount = 0
    visited_dict = {}
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.recurseNumIslands(self, grid, False)

    def recurseNumIslands(self, grid, continuation):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in self.visited_dict:
                    self.visited_dict[(row, col)] = 'visited'
                    if grid[row][col] == 1 and continuation == False:
                        self.islandCount += 1
                        continuation = True
                    
                    elif grid[row][col] == 0:
                        continuation = False
                    # todo: call neighbors recursively with their respective value of continuation

        # print(self.visited_dict)      
    
obj = Solution()
obj.numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])
