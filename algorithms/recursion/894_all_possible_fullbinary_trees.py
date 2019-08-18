# Reference: https://leetcode.com/problems/all-possible-full-binary-trees/
# Approach: Draw trees starting from n = 3 and realize that:
# 1. full binary trees only possible with odd numbers
# 2. solution of 'n' can be retrieved by number of all children in solution 'n-2'
# 3. **Special: When n = 3, 7, 15, 31... => there will be a problem of duplicate counting of full binary trees  if we accept all children (draw and check). Handle that case.

import math
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

class Solution():
    def allPossibleFBT(self, n):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # 'n' has no solution when it is even
        if n % 2 == 0:
            return None
        if n == 1:
            return 1
        # TODO: Put this list check in a separate function or logic
        if n not in [3, 7, 15, 31, 63]:
            return self.allPossibleFBT(n-2) * self.calculateLeafCount(n-2)
        else:
            return self.allPossibleFBT(n-2) * self.calculateLeafCount(n-2) - self.calculateDuplicate(n-2) 
    
    # formula created out of observation
    def calculateLeafCount(self, n):
        return int(n/2) + 1
    
    # formula created out of observation
    def calculateDuplicate(self, n):
        return pow(2, int(math.log(n,2)) - 1)

obj = Solution()
obj.allPossibleFBT(3)   # output: 1


